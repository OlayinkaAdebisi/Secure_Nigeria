from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
# Relative import works perfectly since we are inside the location app
from .models import Location, Feed, High_Risk_Area, Verify

User = get_user_model()

class SecurityAppTests(APITestCase):

    def setUp(self):
        """
        Setup runs before every test. We create a test user and log them in.
        """
        self.user = User.objects.create_user(
            username='testuser', 
            password='testpassword123',
            email='test@example.com'
        )
        self.client.force_authenticate(user=self.user)

        # URLs: naming convention from DefaultRouter
        self.location_url = reverse('location-list')
        self.feed_url = reverse('feed-list')

    def test_create_location_report(self):
        """
        Test that a logged-in user can report a security incident.
        """
        data = {
            "latitude": "6.5244",
            "longitude": "3.3792",
            "state": "LA",
            "local_government": "Mainland",
            "address": "Yaba Tech Junction",
            "incident_types": "ROBBERY",
            "description": "Armed robbery in progress",
            "report_source": "EYEWITNESS"
        }
        
        response = self.client.post(self.location_url, data)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Location.objects.count(), 1)
        # Check that the reported_by field was automatically set to the user
        self.assertEqual(Location.objects.get().reported_by, self.user)
        print("✅ Location Report Test Passed")

    def test_high_risk_area_logic(self):
        """
        Test that High Risk Areas and Feeds are generated correctly.
        """
        # 1. Create a Location (Terrorism = High Risk)
        location = Location.objects.create(
            latitude="12.002", longitude="8.591",
            state="KN", local_government="Kano Municipal",
            address="Market Square", incident_types="TERRORISM",
            description="Serious threat", reported_by=self.user
        )

        # 2. Manually trigger risk creation (simulating your View logic)
        risk_area = High_Risk_Area.objects.create(
            location=location,
            user=self.user,
            description="High Terror Risk",
            risk_level="HIGH",
            risk_types="TERRORISM"
        )

        # 3. Hit the Feed endpoint (which triggers the update_or_create logic in your view)
        response = self.client.get(self.feed_url)
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if a Feed object was automatically created
        self.assertTrue(Feed.objects.filter(risk_area=risk_area).exists())
        print("✅ Feed Generation Logic Test Passed")

    def test_verify_post(self):
        """
        Test that a user can verify a feed item.
        """
        # 1. Setup Data
        location = Location.objects.create(
            latitude="6.5", longitude="3.3", state="LA", 
            local_government="Lagos", address="Test St", 
            reported_by=self.user
        )
        feed = Feed.objects.create(
            author=self.user, location=location, 
            title="Test Alert", content="Danger here",
            created_at="2024-01-01 12:00:00"
        )
        
        # 2. Manual URL Construction based on your paths
        # NOTE: Ensure '/secure_nigeria/' matches the prefix in your main urls.py!
        verify_url = f'/secure_nigeria/feed/verify/{feed.id}/'
        
        response = self.client.post(verify_url)
        
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Verify.objects.count(), 1)
        print("✅ Post Verification Test Passed")