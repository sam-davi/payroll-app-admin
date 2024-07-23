# Generated by Django 5.0.7 on 2024-07-20 04:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_rename_is_current_detail_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_date', models.DateField()),
                ('rate', models.DecimalField(decimal_places=4, max_digits=12)),
                ('rate_type', models.IntegerField(choices=[(2080, 'Hourly'), (260, 'Daily'), (52, 'Weekly'), (26, 'Fortnightly'), (13, 'Fourweekly'), (12, 'Monthly'), (1, 'Annually')], default=2080)),
                ('conversion_method', models.IntegerField(choices=[(364, '52 Weeks per Year'), (365, '365 Days per Year')], default=364)),
                ('hours_per_week', models.DecimalField(decimal_places=3, default=40, max_digits=6)),
                ('days_per_week', models.DecimalField(decimal_places=3, default=5, max_digits=6)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.detail')),
            ],
        ),
    ]
