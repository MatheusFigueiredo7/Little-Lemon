from django.test import TestCase
from django.contrib.auth.models import User
from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class MenuViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='admin', password='Math0103')
        
        MenuItem.objects.create(title="Ice Cream", price=80, inventory=100)
        MenuItem.objects.create(title="Cake", price=50, inventory=50)
        MenuItem.objects.create(title="Pizza", price=95, inventory=75)

    def test_getall(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('menu-items')
        response = self.client.get(url)
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
