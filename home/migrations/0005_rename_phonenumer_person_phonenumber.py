# Generated by Django 3.2 on 2021-06-23 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_product_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='phoneNumer',
            new_name='phoneNumber',
        ),
    ]