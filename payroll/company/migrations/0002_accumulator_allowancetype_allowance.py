# Generated by Django 5.0.7 on 2024-07-21 04:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accumulator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('field_type', models.CharField(choices=[('HOURS', 'Hours'), ('DAYS', 'Days'), ('WEEKS', 'Weeks'), ('QUANTITY', 'Quantity'), ('AMOUNT', 'Amount')], default='AMOUNT', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='AllowanceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('accumulators', models.ManyToManyField(to='company.accumulator')),
            ],
        ),
        migrations.CreateModel(
            name='Allowance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=50)),
                ('display_name', models.CharField(max_length=50)),
                ('allowance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.allowancetype')),
            ],
        ),
    ]
