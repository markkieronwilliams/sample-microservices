import uuid
from rest_framework import status
from rest_framework.test import APITestCase
from attemptapp.models import Attempt


class AttemptsTest(APITestCase):

    def test_create_attempt(self):
        url = '/attempts/'
        data = {'user_id':'3ffc3556-1d72-46c4-9d84-5dc22b5b6aef',
                'score':2000}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Attempt.objects.count(), 1)
        self.assertEqual(Attempt.objects.get().user_id, 
                         uuid.UUID('3ffc3556-1d72-46c4-9d84-5dc22b5b6aef'))
        self.assertEqual(Attempt.objects.get().score, 2000)
