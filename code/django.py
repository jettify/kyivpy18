from django.db import import models

class Question(models.Model):
    def __str__(self):
        return self.question_text


from django.contrib import import admin

from .models import import Question

admin.site.register(Question)

INSTALLED_APPS = [
'django.contrib.admin',
'django.contrib.auth',
'django.contrib.contenttypes',
'django.contrib.sessions',
'django.contrib.messages',
'django.contrib.staticfiles',
]
