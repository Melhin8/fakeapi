# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.defaultfilters import slugify
from django.db import models
import re
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.

class Elfs(models.Model):
    name = models.CharField(max_length=200)
    old = models.PositiveSmallIntegerField()
    genus = models.CharField(max_length=50)
    slug = models.SlugField(max_length=70, unique=True)
    def __str__(self):
        return ("{} {} {} \n").format(self.name, str(self.old), self.genus)
    
    def save(self, **kwargs):
        slug_str = "%s %s %s" % (self.name, self.old, self.genus)
        unique_slugify(self, slug_str)
        super(Elfs, self).save()



def unique_slugify(instance, value, slug_field_name='slug', queryset=None,
                   slug_separator='-'):
    
    slug_field = instance._meta.get_field(slug_field_name)

    slug = getattr(instance, slug_field.attname)
    slug_len = slug_field.max_length

    slug = slugify(value)
    if slug_len:
        slug = slug[:slug_len]
    slug = _slug_strip(slug, slug_separator)
    original_slug = slug

    if queryset is None:
        queryset = instance.__class__._default_manager.all()
    if instance.pk:
        queryset = queryset.exclude(pk=instance.pk)

    next = 2
    while not slug or queryset.filter(**{slug_field_name: slug}):
        slug = original_slug
        end = '%s%s' % (slug_separator, next)
        if slug_len and len(slug) + len(end) > slug_len:
            slug = slug[:slug_len-len(end)]
            slug = _slug_strip(slug, slug_separator)
        slug = '%s%s' % (slug, end)
        next += 1

    setattr(instance, slug_field.attname, slug)


def _slug_strip(value, separator='-'):
    separator = separator or ''
    if separator == '-' or not separator:
        re_sep = '-'
    else:
        re_sep = '(?:-|%s)' % re.escape(separator)
    if separator != re_sep:
        value = re.sub('%s+' % re_sep, separator, value)
    if separator:
        if separator != '-':
            re_sep = re.escape(separator)
        value = re.sub(r'^%s+|%s+$' % (re_sep, re_sep), '', value)
    return value