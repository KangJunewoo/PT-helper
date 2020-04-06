from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime

# User 계정은 카카오톡 API로 email로 취급
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)