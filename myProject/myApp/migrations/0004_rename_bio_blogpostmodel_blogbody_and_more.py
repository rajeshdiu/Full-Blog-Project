# Generated by Django 5.1.2 on 2024-10-19 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_blogpostmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpostmodel',
            old_name='Bio',
            new_name='BlogBody',
        ),
        migrations.AddField(
            model_name='blogpostmodel',
            name='BlogTitle',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
