# Generated by Django 3.1.7 on 2021-04-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instargram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='instargram',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
