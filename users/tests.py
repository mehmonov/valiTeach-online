from django.test import TestCase, Client
from django.urls import reverse
from .models  import User

class LoginTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='12345')
    def test_wrong_login(self):
        for i in range(100):
            with self.subTest(i=i):
                response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpass'})
                self.assertEqual(response.status_code, 200)
    def test_login_get(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)

    def test_login_post(self):
        response = self.client.post(reverse('login'), {'username': 'testuser', 'password': '12345'})
        self.assertEqual(response.status_code, 302)

    def test_login_post_fail(self):
        response = self.client.post(reverse('login'), {'username': 'wronguser', 'password': 'wrongpass'})
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 200)
