from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.test import TestCase

from model_mommy import mommy


class CustomContentTest(TestCase):
    def test_get_absolute_url(self):
        cj = mommy.make('dj_thirdparty.CustomContent', path='/hello/')

        self.assertEqual(cj.get_absolute_url(), '/hello/')

    def test_unicode(self):
        cj = mommy.make(
            'dj_thirdparty.CustomContent', path='/hello/', title='world')

        self.assertEqual(unicode(cj), 'world - /hello/')

    def test_clean_both_exact_and_partial_match(self):
        cj = mommy.make(
            'dj_thirdparty.CustomContent', exact_match=True, partial_match=True)
        message = 'You must set Exact match or Partial match not both.'

        self.assertRaisesMessage(ValidationError, message, cj.clean)

    def test_clean_valid_regex(self):
        cj = mommy.make(
            'dj_thirdparty.CustomContent', exact_match=False,
            partial_match=True, path='^/other/')

        # Running to make sure exception is not thrown
        cj.clean()

    def test_clean_invalid_regex(self):
        cj = mommy.make(
            'dj_thirdparty.CustomContent', exact_match=False,
            partial_match=True, path='][^/other/')
        message = 'unexpected end of regular expression'

        self.assertRaisesMessage(ValidationError, message, cj.clean)

    def test_clean_exact_match_only(self):
        cj = mommy.make(
            'dj_thirdparty.CustomContent', exact_match=False,
            partial_match=False, path='][^/other/')

        # Running to make sure exception is not thrown
        cj.clean()

