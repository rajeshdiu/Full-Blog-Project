# Generated by Django 5.1.2 on 2024-10-19 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0004_rename_bio_blogpostmodel_blogbody_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpostmodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpostmodel',
            name='modified',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
