from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from location.models import Feed
from alert.models import Notification

User = get_user_model()

class SecurityAppTests(APITestCase):

    def setUp(self):
        self.zadi = User.objects.create_user(username='zadi', password='password123')
        self.attacker = User.objects.create_user(username='attacker', password='password123')

        self.post = Feed.objects.create(
            author=self.zadi,
            content="Security Alert in Lagos!",
            location=self.test_location,
        )

        self.comment_url = reverse('comment-list')
        self.profile_url = f'/secure_nigeria/profile/{self.zadi.id}/'

    def test_notification_creation(self):
        self.client.force_authenticate(user=self.attacker)
        
        data = {
            'post': self.post.id,
            'content': 'Is this area safe now?'
        }
        
        response = self.client.post(self.comment_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        count = Notification.objects.filter(recipient=self.zadi, actor=self.attacker).count()
        self.assertEqual(count, 1)

    def test_no_self_notification(self):
        self.client.force_authenticate(user=self.zadi)
        
        data = {
            'post': self.post.id,
            'content': 'Update: The area is clear.'
        }
        
        self.client.post(self.comment_url, data)

        count = Notification.objects.filter(recipient=self.zadi).count()
        self.assertEqual(count, 0)

    def test_profile_security(self):
        self.client.force_authenticate(user=self.attacker)
        
        data = {'phone_number': '08099999999'}
        
        response = self.client.put(self.profile_url, data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
# Create your tests here.
