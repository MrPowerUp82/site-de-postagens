# Generated by Django 2.2.7 on 2021-05-12 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20210512_1855'),
    ]

    operations = [
        migrations.AddField(
            model_name='publica',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='publica',
            name='content',
            field=models.TextField(),
        ),
    ]
