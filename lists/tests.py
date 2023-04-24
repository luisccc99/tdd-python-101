from django.urls import resolve
from django.test import TestCase
from lists.views import home_page

class FooTest(TestCase):

    def test_root_url_resolves_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)