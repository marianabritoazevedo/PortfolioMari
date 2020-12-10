from django.contrib import admin
from .models import Port


class PortAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'published_date'] #o que será listado no admin
	search_fields = ['title', 'slug'] #buscas no admin
	prepopulated_fields = {'slug': ('title',)} #atalho slug a partir do título do post

admin.site.register(Port, PortAdmin)