# Generated by Django 3.1.2 on 2020-11-03 19:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_autor_github'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='descripcion',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='Descripcion'),
            preserve_default=False,
        ),
    ]
