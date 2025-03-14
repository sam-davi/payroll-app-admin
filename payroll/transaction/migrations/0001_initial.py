# Generated by Django 5.0.7 on 2024-07-25 04:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('administration', '0002_alter_paygroup_frequency_alter_payperiod_frequency'),
        ('company', '0008_allowance_unit_type'),
        ('employee', '0012_profile_effective_to'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actual',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=4, max_digits=12)),
                ('unit', models.CharField(choices=[('HOURS', 'Hours'), ('DAYS', 'Days'), ('WEEKS', 'Weeks'), ('QUANTITY', 'Quantity'), ('AMOUNT', 'Amount')], max_length=10)),
                ('hours', models.DecimalField(decimal_places=4, max_digits=12)),
                ('days', models.DecimalField(decimal_places=4, max_digits=12)),
                ('weeks', models.DecimalField(decimal_places=4, max_digits=12)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=12)),
                ('rate_choices', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('allowance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.allowance')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.detail')),
                ('pay_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.payperiod')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Current',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=4, max_digits=12)),
                ('unit', models.CharField(choices=[('HOURS', 'Hours'), ('DAYS', 'Days'), ('WEEKS', 'Weeks'), ('QUANTITY', 'Quantity'), ('AMOUNT', 'Amount')], max_length=10)),
                ('hours', models.DecimalField(decimal_places=4, max_digits=12)),
                ('days', models.DecimalField(decimal_places=4, max_digits=12)),
                ('weeks', models.DecimalField(decimal_places=4, max_digits=12)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=12)),
                ('rate_choices', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('allowance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.allowance')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.detail')),
                ('pay_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.payperiod')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_start', models.DateField()),
                ('period_end', models.DateField()),
                ('date', models.DateField()),
                ('quantity', models.DecimalField(decimal_places=4, max_digits=12)),
                ('unit', models.CharField(choices=[('HOURS', 'Hours'), ('DAYS', 'Days'), ('WEEKS', 'Weeks'), ('QUANTITY', 'Quantity'), ('AMOUNT', 'Amount')], max_length=10)),
                ('hours', models.DecimalField(decimal_places=4, max_digits=12)),
                ('days', models.DecimalField(decimal_places=4, max_digits=12)),
                ('weeks', models.DecimalField(decimal_places=4, max_digits=12)),
                ('rate', models.DecimalField(decimal_places=4, max_digits=12)),
                ('rate_choices', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('allowance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.allowance')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.detail')),
                ('pay_period', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='administration.payperiod')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
