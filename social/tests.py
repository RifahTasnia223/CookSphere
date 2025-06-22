from django.test import TestCase
from .models import UserProfile, Post

class UserProfileModelTest(TestCase):
    def setUp(self):
        self.user_profile = UserProfile.objects.create(
            username='testuser',
            bio='A cooking enthusiast',
            location='Kitchen'
        )

    def test_user_profile_creation(self):
        self.assertEqual(self.user_profile.username, 'testuser')
        self.assertEqual(self.user_profile.bio, 'A cooking enthusiast')
        self.assertEqual(self.user_profile.location, 'Kitchen')

class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title='Delicious Pancakes',
            content='Here is how to make delicious pancakes...',
            author=self.user_profile
        )

    def test_post_creation(self):
        self.assertEqual(self.post.title, 'Delicious Pancakes')
        self.assertIn('pancakes', self.post.content)
        self.assertEqual(self.post.author, self.user_profile)