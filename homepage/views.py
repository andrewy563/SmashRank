# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'homepage/index.html')

def about(request):
	return render(request, 'homepage/index-about.html')
# Create your views here.
