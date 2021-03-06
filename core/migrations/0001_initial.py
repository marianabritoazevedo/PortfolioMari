# Generated by Django 3.1.7 on 2021-03-24 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SobreMim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100, verbose_name='Título')),
                ('titulo_pt_BR', models.CharField(max_length=100, null=True, verbose_name='Título')),
                ('titulo_en_US', models.CharField(max_length=100, null=True, verbose_name='Título')),
                ('texto', models.TextField()),
                ('texto_pt_BR', models.TextField(null=True)),
                ('texto_en_US', models.TextField(null=True)),
            ],
        ),
    ]
