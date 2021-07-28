from http import HTTPStatus
from django.test import TestCase


class PostShareViewTests(TestCase):
    def test_post_success(self):
        # check
        self.assertEqual(response.status_code, HTTPStatus.OK)
        # check


class AddCommentViewTests(TestCase):
    def test_get(self):
        response = self.client.get("/books/add/")

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "<h1>Add Book</h1>", html=True)

    def test_post_success(self):
        url = reverse('')
        response = self.client.post(
            "/books/add/", data={"title": "Dombey and Son"}
        )

        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], "/books/")

    def test_post_error(self):
        response = self.client.post(
            "/books/add/", data={"title": "Dombey & Son"}
        )

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, "Use 'and' instead of '&'", html=True)
