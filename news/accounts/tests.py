from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your tests here.

class UserManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = "testuser",
            email = "testuser@example.com",
            password = "testpass1234",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "testuser@example.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = "testsuperuser",
            email = "testsuperuser@example.com",
            password = "testpass1234",
        )
        self.assertEqual(admin_user.username, "testsuperuser")
        self.assertEqual(admin_user.email, "testsuperuser@example.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)

class SignupPageTests(TestCase):
    def test_url_exists_at_correct_location_signupview(self): #checks our signup URL is at the correct position
        response = self.client.get("/accounts/signup/")
        self.assertEqual(response.status_code, 200)

    def test_signup_view_name(self): #checks if singup.html is being used
        response = self.client.get(reverse("signup"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response, "registration/signup.html")

    def test_signup_form(self): #checks our form by sending a post request to fill it out
        response = self.client.post( #we send these values of username etc and then later check if they are recorded correctly
            reverse("signup"),
            {
                "username":"testuser",
                "email":"testuser@email.com",
                "password1":"testpass123",
                "password2":"testpass123",
            }
        )
        #code below this checks the data we put in the form with a post request is recorded correctly
        self.assertEqual(response.status_code,302)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username, "testuser")
        self.assertEqual(
            get_user_model().objects.all()[0].email, "testuser@email.com"
        )
