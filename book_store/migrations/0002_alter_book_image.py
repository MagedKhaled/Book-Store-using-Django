# Generated by Django 4.2.6 on 2023-10-12 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(max_length=200, upload_to='book_store/images/'),
        ),
    ]