try:
    from mock import patch, call
except ImportError:
    from unittest.mock import patch, call

from django.test import TestCase
from accounts.models import Token

class SendLoginEmailViewTest(TestCase):

    def test_redirects_to_home_page(self):
        response = self.client.post('/accounts/send_login_email', data={
            'email': 'edith@example.com'
        })
        self.assertRedirects(response, '/')