from django.test import TestCase
from django.contrib.auth import get_user_model #refers to the user
from .models import Post
from django.urls import reverse
# Create your tests here.

class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "testuser", email = "test@email.com", password = "secret"
        )

        cls.post = Post.objects.create(
            title = "A Good title",
            body = "Nice body content",
            author = cls.user,
        )

    def test_post_model(self):
        self.assertEqual(self.post.title, "A Good title")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(str(self.post), "A Good title")
        self.assertEqual(self.post.get_absolute_url(),"/post/1/")

    def test_url_exists_at_correct_location_listview(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code,200)

    def test_url_exists_at_correct_location_detailview(self):
        response = self.client.get("/post/1/")
        self.assertEqual(response.status_code,200)

    def test_post_listview(self):
        response = self.client.get(reverse("home")) #saves the URL with name "home" in the response variable
        self.assertEqual(response.status_code,200) #checks if the url with the name "home" is used
        self.assertContains(response, "Nice body content") #checks content
        self.assertTemplateUsed(response,"home.html") #checks if the template is used

    def test_post_detailview(self):
        response = self.client.get(reverse("post_detail",kwargs = {"pk": self.post.pk})) #saves the url with the name "post_detail" with primary key as its key arguments
        no_response = self.client.get("/post/100000/") #saves what we do not want to see as a response
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code,404) #checks if the response we dont want to see is an error or not
        self.assertContains(response, "A Good title")
        self.assertTemplateUsed(response, "post_detail.html")

    def test_post_createview(self):
        response = self.client.post(reverse("post_new"),{
            "title": "New title",
            "body": "New text",
            "author": self.user.id,
        },)
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title, "New title") #.last() revers to the last object created in our model, we did that above by post method
        self.assertEqual(Post.objects.last().body, "New text")

    def test_post_updateview(self):
        response = self.client.post(reverse("post_edit", args = "1"),{
            "title":"Updated title",
            "body": "Updated text",
        },)
        self.assertEqual(response.status_code,302)
        self.assertEqual(Post.objects.last().title, "Updated title")
        self.assertEqual(Post.objects.last().body, "Updated text")

    def test_post_deleteview(self):
        response = self.client.post(reverse("post_delete", args = "1"))
        self.assertEqual(response.status_code, 302)
