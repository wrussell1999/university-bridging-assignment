from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest

from cv.views import cv_page

class CvTest(TestCase):

    def test_cv_page(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_page)

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith(''))
        self.assertIn('<title>Will Russell | CV</title>', html)
        self.assertTrue(html.endswith('</html>'))

    def test_cv_page_sections(self):
        