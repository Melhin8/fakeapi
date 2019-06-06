# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Elfs
# Register your models here.
class ElfsAdmin(admin.ModelAdmin):
    list_display = ('name', 'old', 'genus')
    list_filter = ['name', 'old', 'genus']
    search_fields = ['name', 'old', 'genus']

admin.site.register(Elfs, ElfsAdmin)