# Generated by Django 3.1.3 on 2020-12-02 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_prefeito_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prefeito',
            name='foto',
        ),
    ]