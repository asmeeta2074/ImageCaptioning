# Generated by Django 2.2.2 on 2019-06-21 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usercaption', '0007_imagecaption_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecaption',
            name='image',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
    ]
