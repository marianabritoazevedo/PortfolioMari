from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.
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