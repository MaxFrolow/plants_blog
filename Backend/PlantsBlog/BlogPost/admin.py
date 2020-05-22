from django.contrib import admin

from .models import PlantPost

@admin.register(PlantPost)
class PostAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'id', 'created', 'updated', 'is_favorite']
    list_filter = ['id', 'title', 'created', 'updated', 'is_favorite']
    search_fields = ['title', 'text', 'created', 'id', 'is_favorite']

