# Generated by Django 3.0.5 on 2024-02-01 19:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('insurance_company', '0001_initial'),
        ('tameenak_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('amount', models.FloatField(blank=True, null=True)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_status', models.CharField(blank=True, choices=[('paid', 'Paid'), ('unpaid', 'Unpaid')], max_length=50, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tameenak_user.TameenakCustomer')),
                ('insurance_company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insurance_company.InsuranceCompany')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
