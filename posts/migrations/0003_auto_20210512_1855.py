# Generated by Django 2.2.7 on 2021-05-12 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_publica_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publica',
            name='author',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
