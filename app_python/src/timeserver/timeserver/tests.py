import datetime
import json

from django.test import TestCase
from rest_framework.test import APIClient


class TimeServerTestCase(TestCase):
    def setUp(self):
        # Setup run before every test method.
        pass

    def tearDown(self):
        # Clean up run after every test method.
        pass

    def test_index(self):
        """
        Ensure index page is returned with 200 status code
        """
        client = APIClient()
        response = client.get('/')
        self.assertTrue(response.status_code == 200)

    def test_current_time_api(self):
        """
        Ensure current time API endpoint response is returned with 200 status code and returned time does not differ from
        the current one in more than a second.
        """
        client = APIClient()
        response = client.get('/current_time/')
        self.assertTrue(response.status_code == 200)
        self.assertTrue(
            (datetime.datetime.now(datetime.timezone.utc) -
             datetime.datetime.fromisoformat(
                 json.loads(
                     str(response.content, 'utf-8')
                 )['current_time']
             )).total_seconds() <= 1
        )
