from django.contrib import admin
from .models import Port, Certificado, PortfolioOK, CertificadoOK


class PortAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'published_date'] #o que será listado no admin
	search_fields = ['title', 'slug'] #buscas no admin
	prepopulated_fields = {'slug': ('title',)} #atalho slug a partir do título do post

class PortfolioOKAdmin(admin.ModelAdmin):
	list_display = ['titulo_port', 'slug', 'published_date'] #o que será listado no admin
	search_fields = ['titulo_port', 'slug'] #buscas no admin
	prepopulated_fields = {'slug': ('titulo_port',)} #atalho slug a partir do título do post

class CertificadoAdmin(admin.ModelAdmin):
	list_display = ['title', 'slug', 'published_date'] #o que será listado no admin
	search_fields = ['title', 'slug'] #buscas no admin
	prepopulated_fields = {'slug': ('title',)} #atalho slug a partir do título do post

class CertificadoAdminOK(admin.ModelAdmin):
	list_display = ['titulo_port', 'slug', 'published_date'] #o que será listado no admin
	search_fields = ['titulo_port', 'slug'] #buscas no admin
	prepopulated_fields = {'slug': ('titulo_port',)} #atalho slug a partir do título do post

admin.site.register(Port, PortAdmin)
admin.site.register(Certificado, CertificadoAdmin)
admin.site.register(PortfolioOK, PortfolioOKAdmin)
admin.site.register(CertificadoOK, CertificadoAdminOK)