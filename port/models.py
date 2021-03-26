from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

class Port(models.Model):
    img_card = models.ImageField(upload_to='port/images', verbose_name='Imagem Card', null=True, blank=True)
    img_1 = models.ImageField(upload_to='port/images', verbose_name='Imagem 1', null=True, blank=True)
    img_2 = models.ImageField(upload_to='port/images', verbose_name='Imagem 2', null=True, blank=True)
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Atalho')
    text = models.TextField('Texto')
    tecnologias = models.TextField('Tecnologias', null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    link_rep = models.CharField('Link Git', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('port:details', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Postagem'
        verbose_name_plural = 'Postagens'
        ordering = ['published_date']

class PortfolioOK(models.Model):
    img_card = models.ImageField(upload_to='port/images', verbose_name='Imagem Card', null=True, blank=True)
    img_1 = models.ImageField(upload_to='port/images', verbose_name='Imagem 1', null=True, blank=True)
    img_2 = models.ImageField(upload_to='port/images', verbose_name='Imagem 2', null=True, blank=True)
    titulo_port = models.CharField('Título português', max_length=200)
    titulo_ing = models.CharField('Título inglês', max_length=200)
    slug = models.SlugField('Atalho')
    texto_port = models.TextField('Texto português')
    texto_ing = models.TextField('Texto inglês')
    tecnologias = models.TextField('Tecnologias', null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)
    link_rep = models.CharField('Link Git', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo_port
    
    def get_absolute_url(self):
        return reverse('port:details', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Postagem OK'
        verbose_name_plural = 'Postagens OK'
        ordering = ['published_date']


class Certificado(models.Model):
    img = models.ImageField(upload_to='port/images', verbose_name='Imagem certificado', null=True, blank=True)
    title = models.CharField('Título', max_length=200)
    slug = models.SlugField('Atalho')
    descricao = models.TextField('Texto')
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('port:certificado_details', args=[str(self.slug)])
    
    class Meta:
        verbose_name = 'Certificado'
        verbose_name_plural = 'Certificados'
        ordering = ['published_date']

class CertificadoOK(models.Model):
    img = models.ImageField(upload_to='port/images', verbose_name='Imagem certificado', null=True, blank=True)
    titulo_port = models.CharField('Título português', max_length=200)
    titulo_ing = models.CharField('Título inglês', max_length=200)
    slug = models.SlugField('Atalho')
    descricao_port = models.TextField('Texto português')
    descricao_ing = models.TextField('Texto inglês')
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.titulo_port

    def get_absolute_url(self):
        return reverse('port:certificado_details', args=[str(self.slug)])
    
    class Meta:
        verbose_name = 'Certificado OK'
        verbose_name_plural = 'Certificados OK'
        ordering = ['published_date']