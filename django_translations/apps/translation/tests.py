import json

from django.urls import reverse
from rest_framework import status

from rest_framework.test import APITestCase

from .models import PostTranslation, Post


class APIBaseTestCase(APITestCase):
    pass


class TranslationViewSetTest(APIBaseTestCase):
    pass


class PostViewSetTest(APIBaseTestCase):
    """
    Test post view set
    """

    def setUp(self):
        super().setUp()
        self.url = reverse('api:post-list')
        self.create_post()

    def create_post(self):
        self.post = Post.objects.create(slug='test')
        self.translations = PostTranslation.objects.bulk_create(
            [
                PostTranslation(title='tk title 1', body='tk body 2', language_code='tk', master_id=self.post.pk),
                PostTranslation(title='en title 1', body='en body 2', language_code='en', master_id=self.post.pk),
                PostTranslation(title='ru title 1', body='ru body 2', language_code='ru', master_id=self.post.pk),
            ]
        )
        self.url_detail = reverse('api:post-detail', kwargs={'pk': self.post.pk})

    def test_get_post_list(self):
        """
        Test post list api view
        """
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post_list(self):
        """
        Test update post list
        """
        data = {
            "slug": "test",
            "translations": {
                "tk": {
                    "title": "tk read",
                    "body": "tk body"
                },
                "ru": {
                    "title": "Cicero",
                    "body": "fds"
                },
            }
        }

        response = self.client.patch(self.url_detail, data=json.dumps(data), content_type='application/json')

        print('\n',response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

