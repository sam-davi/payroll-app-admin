# Generated by Django 5.0.7 on 2024-07-23 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_remove_allowancetype_accumulators_accumulatormember'),
    ]

    operations = [
        migrations.AddField(
            model_name='allowancetype',
            name='accumulators',
            field=models.ManyToManyField(blank=True, through='company.AccumulatorMember', to='company.accumulator'),
        ),
    ]
