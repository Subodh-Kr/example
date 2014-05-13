from django.db import models

class Userprofile(models.Model):
	nick = models.CharField(max_length = 50)
	email = modes.EmailField()