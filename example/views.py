#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.contrib.auth.models import User

def home(request):
	"""
	This view is for the basic landing page of the website.
	"""
	# declare some variables here and use them in index.html
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))