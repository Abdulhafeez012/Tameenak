# Generated by Django 3.0.5 on 2024-02-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insurance_company', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insurancecompany',
            name='logo',
            field=models.ImageField(default='insurance_company/logo/default_logo.png', upload_to='insurance_company/logo/'),
        ),
    ]
