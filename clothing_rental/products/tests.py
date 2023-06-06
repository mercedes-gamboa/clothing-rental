# from django.contrib.auth import get_user_model
# from django.test import TestCase
# from django.urls import reverse
#
# from products.models import Inventory
#
# User = get_user_model()
# # Create your tests here.
#
# class InventoryListViewTestCase(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         cls.user = User.objects.create_user(username="test123", email="test@test.com", password="secret", is_staff=True)
#
#         cls.inventory = Inventory.objects.create(
#             detail="this is a description",
#             code ="CCDO 099",
#             price=10.00,
#         )
#
#     def sefUp(self) -> None:
#         self.client.force_login(self.user)
#
#     def test_not_logged_in_user_redirect_to_login(self):
#         self.client.logout()
#         response = self.client.get(reverse("main/home"))
#
#         self.assertEquals(response.status_code, 302)
