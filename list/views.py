# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
from django.views import generic
from django.forms import ModelForm
from django.http import HttpResponseRedirect

from list.models import Elfs
from list.forms import AddForm, SearchForm, Sort

# Create your views here.
def index(request):
    return render(request, 'list/index.html')

def listt(request):
    list_of_elfs = Elfs.objects.all()
    context = {'list_of_elfs':list_of_elfs}
    return render(request, 'list/list.html', context)
    #return render(request, 'list/list.html', {'list_of_elfs': Elfs.objects.all()})

def add(request):
    submitted = False
    if request.method == 'POST':
      form = AddForm(request.POST)
      if form.is_valid():
            form.save()
            return HttpResponseRedirect('/elfs/add/?submitted=True')
    else:
            form = AddForm()
            if 'submitted' in request.GET:
                  submitted = True
    return render(request, 'list/add.html', {'form': form, 'submitted': submitted})

def search(request):
    submitted = False
    if request.method == 'GET':
      form = SearchForm(request.GET)
      if form.is_valid():
            name = form.cleaned_data['name']
            find = Elfs.objects.filter(name = name)
            if find.exists():
                return HttpResponse(find)
            else:
                submitted = True
                #return HttpResponse('No elf')
                return HttpResponseRedirect('/elfs/search/?submitted=True')
    else:
          form = SearchForm()

    return render(request, 'list/search.html', {'form': form, 'submitted': submitted})
    
def list(request):
      if request.method == 'GET':
          form = Sort(request.GET)
          if form.is_valid():
                q = form.cleaned_data['sort']
                list_of_elfs = Elfs.objects.order_by(q)
                context = {'list_of_elfs':list_of_elfs}
                return render(request, 'list/list.html', context)
      else:
            form = Sort()

      return render(request, 'list/list.html', {'form': form})

def detail(request, slug):
      q = Elfs.objects.filter(slug__iexact = slug) 
      if q.exists(): 
	      return HttpResponse(q)
      else: 
	      return HttpResponse('<h1>Elf Not Found</h1>') 