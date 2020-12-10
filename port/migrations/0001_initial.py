# Generated by Django 3.1.4 on 2020-12-08 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_card', models.ImageField(blank=True, null=True, upload_to='port/images', verbose_name='Imagem Card')),
                ('img_1', models.ImageField(blank=True, null=True, upload_to='port/images', verbose_name='Imagem 1')),
                ('img_2', models.ImageField(blank=True, null=True, upload_to='port/images', verbose_name='Imagem 2')),
                ('title', models.CharField(max_length=200, verbose_name='Título')),
                ('slug', models.SlugField(verbose_name='Atalho')),
                ('text', models.TextField(verbose_name='Texto')),
                ('published_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('link_rep', models.CharField(blank=True, max_length=200, null=True, verbose_name='Link Git')),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
                'ordering': ['published_date'],
            },
        ),
    ]
