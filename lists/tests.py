from django.test import TestCase

class FooTest(TestCase):

    def test_should_fail(self):
        self.assertEqual(1 + 1, 3)