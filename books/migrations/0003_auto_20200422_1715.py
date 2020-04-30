# Generated by Django 3.0.5 on 2020-04-22 11:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_books_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='condition',
            field=models.CharField(default=django.utils.timezone.now, max_length=130),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.TextField(default='hello world'),
            preserve_default=False,
        ),
    ]
