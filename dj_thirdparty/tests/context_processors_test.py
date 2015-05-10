from django.test.client import RequestFactory
from django.test import TestCase

from model_mommy import mommy

from dj_thirdparty.context_processors import custom_content, fetch_objects


class CustomContentContextProcessor(TestCase):
    def setUp(self):
        self.request = RequestFactory().get('/')

    def test_no_request(self):
        self.assertEqual(custom_content(None), {})

    def test_request_no_data(self):
        self.assertEqual(
            custom_content(self.request)['custom_javascript_footer'], '')

    def test_request_custom_content(self):
        js = "alert('hello world');"

        mommy.make(
            'dj_thirdparty.CustomContent', active=True, javascript=js,
            path="/")

        self.assertEqual(
            custom_content(self.request)['custom_javascript_footer'], js)

    def test_request_custom_content_not_active(self):
        js = "alert('hello world');"

        mommy.make(
            'dj_thirdparty.CustomContent', active=False, javascript=js,
            path="/")

        self.assertEqual(
            custom_content(self.request)['custom_javascript_footer'], '')

    def test_fetch_objects(self):
        self.maxDiff = 2056
        cj1 = mommy.make('dj_thirdparty.CustomContent', path='all')
        cj2 = mommy.make(
            'dj_thirdparty.CustomContent', path='/other/misc/',
            exact_match=True)
        cj3 = mommy.make(
            'dj_thirdparty.CustomContent', path='/homeservice/',
            partial_match=True, exact_match=False)
        cj4 = mommy.make(
            'dj_thirdparty.CustomContent', path='/', exact_match=True)
        cj5 = mommy.make(
            'dj_thirdparty.CustomContent', path='all', header=True)
        cj6 = mommy.make(
            'dj_thirdparty.CustomContent', path='/other/',
            exact_match=True, header=True)
        cj7 = mommy.make(
            'dj_thirdparty.CustomContent', path='/homes/',
            partial_match=True, exact_match=False, header=True)
        cj8 = mommy.make(
            'dj_thirdparty.CustomContent', path='/', exact_match=True,
            header=True)

        data = {'all_urls': {'header': [cj5], 'footer': [cj1]},
                'exact_urls': {'header': [cj8, cj6], 'footer': [cj4, cj2]},
                'partial_urls': {'header': [cj7], 'footer': [cj3]}}

        self.assertEqual(fetch_objects(), data)

    def test_get_exact(self):
        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='/')
        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text2', path='/other/')

        self.assertEqual(
            custom_content(self.request)['custom_javascript_footer'], 'text1')

    def test_get_exact_no_match(self):
        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='/other1/')
        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text2', path='/other2/')

        self.assertEqual(
            custom_content(self.request)['custom_javascript_footer'], '')

    def test_get_partial_exact_match(self):
        request = RequestFactory().get('/other/')

        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='^/other/',
            exact_match=False, partial_match=True)

        self.assertEqual(
            custom_content(request)['custom_javascript_footer'], 'text1')

    def test_get_partial_partial_match(self):
        request = RequestFactory().get('/other/misc/')

        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='^/other/',
            exact_match=False, partial_match=True)

        self.assertEqual(
            custom_content(request)['custom_javascript_footer'], 'text1')

    def test_get_partial_no_match_similar_path(self):
        request = RequestFactory().get('/home/other/')

        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='^/home/')

        self.assertEqual(
            custom_content(request)['custom_javascript_footer'], '')

    def test_get_partial_no_match(self):
        request = RequestFactory().get('/other/')

        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='^/misc/')

        self.assertEqual(
            custom_content(request)['custom_javascript_footer'], '')

    def test_get_exact_header(self):
        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='/',
            header=True)
        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text2', path='/other/',
            header=True)

        self.assertEqual(
            custom_content(self.request)['custom_javascript_header'],
            'text1')

    def test_get_exact_no_match_header(self):
        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='/other/',
            header=True)
        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text2', path='/misc/',
            header=True)

        self.assertEqual(
            custom_content(self.request)['custom_javascript_header'], '')

    def test_get_partial_exact_match_header(self):
        request = RequestFactory().get('/other/')

        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='^/other/',
            exact_match=False, partial_match=True, header=True)

        self.assertEqual(
            custom_content(request)['custom_javascript_header'], 'text1')

    def test_get_partial_partial_match_header(self):
        request = RequestFactory().get('/other/misc/')

        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1', path='^/other/',
            exact_match=False, partial_match=True, header=True)

        self.assertEqual(
            custom_content(request)['custom_javascript_header'], 'text1')

    def test_get_partial_no_match_similar_path_header(self):
        request = RequestFactory().get('/other/misc/')

        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1',
            path='^/other/', header=True)

        self.assertEqual(
            custom_content(request)['custom_javascript_header'], '')

    def test_get_partial_no_match_header(self):
        request = RequestFactory().get('/other/')

        mommy.make(
            'dj_thirdparty.CustomContent', javascript='text1',
            path='^/misc/', header=True)

        self.assertEqual(
            custom_content(request)['custom_javascript_header'], '')
