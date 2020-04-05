from django.contrib import admin
from .models import PDF, Quecard

# admin customizing
@admin.register(PDF) # decorator 형태로 등록
class StoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'author', 'pdffile', 'text', 'written_date', 'latest_date', 'category']

@admin.register(Quecard)
class StoryAdmin(admin.ModelAdmin):
	list_display = ['pdffile', 'image', 'sequence', 'text', 'time_min', 'time_sec']