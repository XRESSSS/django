# Generated by Django 5.0.2 on 2024-02-19 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to='books.author'),
        ),
    ]
