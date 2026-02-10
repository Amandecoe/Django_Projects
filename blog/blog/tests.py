from django.test import TestCase
from django.contrib.auth import get_user_model #refers to the user
from .models import Post
# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "testuser", email = "test@email.com", password = "secret"
        )

        cls.post = Post.objects.create(
            title = "A Good title",
            body = "Nice Body Content",
            author = cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A Good title")
        self.assertEqual(self.post.body, "Nice Body Content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A Good title")
        self.assertEqual(self.post.get_absolute_url(),"/post/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)
