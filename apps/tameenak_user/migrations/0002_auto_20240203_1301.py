# Generated by Django 3.0.5 on 2024-02-03 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tameenak_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tameenakcustomer',
            name='picture',
            field=models.ImageField(default='tameenak_user/default_pic.png', upload_to='tameenak_user/tameenak_customer/profile_pic'),
        ),
    ]