# Generated by Django 3.0.5 on 2020-04-25 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectmodel',
            name='image',
            field=models.ImageField(height_field=200, upload_to='proj_images', width_field=200),
        ),
    ]