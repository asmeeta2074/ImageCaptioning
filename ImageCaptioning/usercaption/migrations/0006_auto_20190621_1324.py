# Generated by Django 2.2.2 on 2019-06-21 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usercaption', '0005_auto_20190621_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecaption',
            name='image',
        ),
        migrations.AddField(
            model_name='imagecaption',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='imagecaption',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='imagecaption',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
