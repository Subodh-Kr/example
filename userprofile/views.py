#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.template.context import Context, RequestContext
from django.shortcuts import render_to_response, redirect
from django.conf import settings
from django.contrib.auth.models import User

def profile(request):
	if request.method == "POST":
		x = request.POST.get('username',"blah!!")
		users = User.objects.get(username=x)
		username = users[0].password
	else:
		username = "blah!!"
	return render_to_response("example.html", locals(), context_instance = RequestContext(request))
