# Generated by Django 4.0.5 on 2022-06-25 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_projectimages_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='mainImage',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
