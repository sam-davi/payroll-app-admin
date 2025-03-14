# Generated by Django 5.0.7 on 2024-10-02 03:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('company', '0008_allowance_unit_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Roster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('cycle_length', models.IntegerField(default=7)),
                ('rate_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.ratetype')),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('start_time_minutes', models.IntegerField(default=510)),
                ('end_time_minutes', models.IntegerField(default=1020)),
                ('break_start_minutes', models.IntegerField(default=720)),
                ('break_end_minutes', models.IntegerField(default=750)),
                ('paid_break', models.BooleanField(default=False)),
                ('rate_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.ratetype')),
            ],
        ),
        migrations.CreateModel(
            name='RosterShift',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift_number', models.IntegerField()),
                ('roster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.roster')),
                ('shift', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roster.shift')),
            ],
        ),
        migrations.AddField(
            model_name='roster',
            name='shifts',
            field=models.ManyToManyField(through='roster.RosterShift', to='roster.shift'),
        ),
    ]
