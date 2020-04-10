from django.contrib import admin
from .models import Profile

# admin customizing
@admin.register(Profile) # decorator 형태로 등록
class StoryAdmin(admin.ModelAdmin):
	list_display = ['email', 'name']