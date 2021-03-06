# Generated by Django 3.1.7 on 2021-03-25 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_sobremim'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormacaoAcademica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitulo_port', models.CharField(max_length=100, verbose_name='Subtítulo português')),
                ('subtitulo_ing', models.CharField(max_length=100, verbose_name='Subtítulo português')),
                ('texto_port', models.TextField(verbose_name='Texto português')),
                ('texto_ing', models.TextField(verbose_name='Texto inglês')),
            ],
        ),
        migrations.CreateModel(
            name='FormacaoComplementar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitulo_port', models.CharField(max_length=100, verbose_name='Subtítulo português')),
                ('subtitulo_ing', models.CharField(max_length=100, verbose_name='Subtítulo português')),
                ('texto_port', models.TextField(verbose_name='Texto português')),
                ('texto_ing', models.TextField(verbose_name='Texto inglês')),
            ],
        ),
        migrations.CreateModel(
            name='FormacaoProfissional',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtitulo_port', models.CharField(max_length=100, verbose_name='Subtítulo português')),
                ('subtitulo_ing', models.CharField(max_length=100, verbose_name='Subtítulo português')),
                ('texto_port', models.TextField(verbose_name='Texto português')),
                ('texto_ing', models.TextField(verbose_name='Texto inglês')),
            ],
        ),
        migrations.DeleteModel(
            name='Formacao',
        ),
    ]
