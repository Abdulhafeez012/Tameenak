# Generated by Django 3.0.5 on 2024-02-03 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_company', '0002_auto_20240203_1722'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompany',
            name='logo',
            field=models.ImageField(default='image/insurance_company/logo/default_logo.png', upload_to='image/insurance_company/logo/'),
        ),
    ]
