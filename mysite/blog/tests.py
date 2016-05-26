from django.test import TestCase
from django.utils import timezone
from .models import Post

# Create your tests here.
class PostTestCase(TestCase):
    def edited_date_before_post(self):
        self.assertEqual(fake_test(), False)
