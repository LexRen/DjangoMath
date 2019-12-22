from __future__ import unicode_literals

from django.db import models

from django.contrib.auth.models import User

class basede2(models.Model):
	created_by = models.ForeignKey(User, on_delete=models.CASCADE)
	edad = models.IntegerField()
	