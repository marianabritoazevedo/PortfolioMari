# Generated by Django 3.1.7 on 2021-03-25 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_port', models.CharField(max_length=100, verbose_name='Título')),
                ('titulo_ing', models.CharField(max_length=100, verbose_name='Título')),
            ],
        ),
        migrations.DeleteModel(
            name='SobreMim',
        ),
    ]