from api.tasks import send_email_notifications
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class LoggedInTestTemplate(APITestCase):
    def setUp(self):
        super().setUp()
        user = User.objects.create_user(
            username="admin", email="admin@restaurant-menu.com", password="start1234", is_superuser=True
        )
        self.user = user
        self.client.login(username="admin", password="start1234")


class DishTestsAuthenticated(LoggedInTestTemplate):
    """Tests REST API available for authenticated users."""

    def setUp(self):
        user = User.objects.create_user(
            username="admin", email="admin@restaurant-menu.com", password="start1234", is_superuser=True
        )
        self.user = user
        self.client.login(username="admin", password="start1234")

    def test_create_dish(self):
        url = reverse("api:dishes-list")
        data = {
            "name": "Danie testowe",
            "description": "Opis testowy",
            "price": "10.0",
            "preparation_time": 1,
            "is_vegan": "true",
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class DishTestsPublic(APITestCase):
    """Tests REST API available for all users."""

    def test_get_dish(self):
        url = reverse("api:dishes-detail", kwargs={"pk": 1})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Jajecznica")

    def test_get_dishes(self):
        url = reverse("api:dishes-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class MenuTestsAuthenticated(LoggedInTestTemplate):
    """Tests REST API available for authenticated users."""

    def setUp(self):
        user = User.objects.create_user(
            username="admin", email="admin@restaurant-menu.com", password="start1234", is_superuser=True
        )
        self.user = user
        self.client.login(username="admin", password="start1234")

    def test_get_menus(self):
        url = reverse("api:menus-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)


class MenuTestsPublic(APITestCase):
    """Tests REST API available for all users."""

    def test_get_menu(self):
        url = reverse("api:menus-detail", kwargs={"pk": 2})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Śniadaniowe")

    def test_get_menus(self):
        url = reverse("api:menus-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)  # don't display empty menus

    def test_get_menus_sort_name(self):
        url = reverse("api:menus-list")
        response = self.client.get(url, {"sort": "name"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Kolacyjne")

    def test_get_menus_sort_num_dishes(self):
        url = reverse("api:menus-list")
        response = self.client.get(url, {"sort": "num_dishes"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Śniadaniowe")

    def test_get_menus_filter_name(self):
        url = reverse("api:menus-list")
        response = self.client.get(url, {"name": "Śniadaniowe"}, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["name"], "Śniadaniowe")


class CeleryTests(LoggedInTestTemplate):
    def test_send_email_notification(self):
        message = send_email_notifications(test=True)
        self.assertIn("admin", message)
