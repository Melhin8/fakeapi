# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def login(request):
    return render(request, 'social/login.html')

@login_required
def home(request):
    return render(request, 'social/home.html')
# Create your views here.
