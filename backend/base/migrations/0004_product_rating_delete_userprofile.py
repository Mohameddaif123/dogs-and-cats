# Generated by Django 5.0.4 on 2024-05-08 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='rating',
            field=models.FloatField(default=0.0),
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
