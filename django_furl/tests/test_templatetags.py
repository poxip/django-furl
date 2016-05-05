from django.test import TestCase

from django_furl.templatetags.furl_tags import furl_update, furl_add, furl_del


class FurlTagsTest(TestCase):

    base_url = 'http://example.com'

    def test_url_add_simple(self):
        params = {
            'q': 'series',
            'name': 'Dwight'
        }
        result = str(furl_add(self.base_url, **params))

        self.assertIn('q=series', result)
        self.assertIn('name=Dwight', result)

    def test_url_add_extended(self):
        params = {
            'q': 'stuff',
            'title': 'The Office',
            'list': 'two'
        }
        url = self.base_url + '/?q=series&name=Dwight&list=one'
        result = str(furl_add(url, **params))

        self.assertIn('q=stuff', result)
        self.assertIn('title=The+Office', result)
        self.assertIn('name=Dwight', result)
        self.assertIn('list=one', result)
        self.assertIn('list=two', result)

    def test_url_del(self):
        url = self.base_url + '/?q=dump&foo=bar'
        result = str(furl_del(url, 'q'))
        self.assertIn('foo=bar', result)
        self.assertNotIn('q=dump', result)

    def test_url_update(self):
        params = {
            'q': 'fun'
        }
        url = self.base_url + '/?q=bar'
        result = str(furl_update(url, **params))
        self.assertIn('q=fun', result)
        self.assertNotIn('q=bar', result)
