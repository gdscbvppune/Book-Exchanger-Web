# Generated by Django 3.0.5 on 2020-04-22 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='author',
            field=models.CharField(max_length=150, null=True),
        ),
    ]