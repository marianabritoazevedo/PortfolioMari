from django.db import models

class SobreMim(models.Model):
    titulo_port = models.CharField('Título português', max_length=100)
    titulo_ing = models.CharField('Título Inglês', max_length=100)
    texto_port = models.TextField()
    texto_ing = models.TextField()

    def __str__(self):
        return self.titulo_port

class FormacaoAcademica(models.Model):
    subtitulo_port = models.CharField('Subtítulo português', max_length=100)
    subtitulo_ing = models.CharField('Subtítulo inglês', max_length=100)
    texto_port = models.TextField('Texto português')
    texto_ing = models.TextField('Texto inglês')

    def __str__(self):
        return self.subtitulo_port

class FormacaoProfissional(models.Model):
    subtitulo_port = models.CharField('Subtítulo português', max_length=100)
    subtitulo_ing = models.CharField('Subtítulo inglês', max_length=100)
    texto_port = models.TextField('Texto português')
    texto_ing = models.TextField('Texto inglês')

    def __str__(self):
        return self.subtitulo_port

class FormacaoComplementar(models.Model):
    subtitulo_port = models.CharField('Subtítulo português', max_length=100)
    subtitulo_ing = models.CharField('Subtítulo inglês', max_length=100)
    texto_port = models.TextField('Texto português')
    texto_ing = models.TextField('Texto inglês')

    def __str__(self):
        return self.subtitulo_port

class CardPortfolio(models.Model):
    img_card = models.ImageField(upload_to='port/images', verbose_name='Imagem Card', null=True, blank=True)
    titulo_port = models.CharField('Título português', max_length=100)
    titulo_ing = models.CharField('Título Inglês', max_length=100)
    subtitulo_port = models.CharField('Subtítulo português', max_length=300)
    subtitulo_ing = models.CharField('Subtítulo inglês', max_length=300)
    modal_port = models.TextField('Texto modal português')
    modal_ing = models.TextField('Texto modal inglês')

    def __str__(self):
        return self.titulo_port
