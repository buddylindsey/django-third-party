import re
from django.db import models
from django.core.exceptions import ValidationError
from django.utils.encoding import python_2_unicode_compatible

from django_extensions.db.models import TimeStampedModel


@python_2_unicode_compatible
class CustomContent(TimeStampedModel):
    title = models.CharField(max_length=255, blank=True)
    path = models.CharField(
        max_length=255, blank=True,
        help_text=('URL you want to use, python regular experssion, or '
                   'constant "all"'))
    css = models.TextField(blank=True)
    javascript = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    exact_match = models.BooleanField(
        default=True, help_text=('Used when you want to add a code snippet to'
                                 ' a specific page only.'))
    partial_match = models.BooleanField(
        default=False, help_text=('Used when you want to add a code snippet to'
                                  ' a lot of pages based on a regex.'))
    header = models.BooleanField(
        default=False, help_text=('Set javascript to be in the head.'
                                  ' Otherwise it will be in the footer'))

    def __str__(self):
        return u'{} - {}'.format(self.title, self.path)

    def get_absolute_url(self):
        return self.path

    def clean(self):
        if self.exact_match and self.partial_match:
            raise ValidationError('You must set Exact match or Partial match '
                                  'not both.')

        if self.partial_match:
            try:
                re.compile(self.path)
            except re.error as ex:
                raise ValidationError(str(ex))
