# Generated by Django 5.0.7 on 2024-07-24 05:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_customdatefield_customnumberfield_customtextfield_and_more'),
        ('employee', '0009_additionaldatedetail_additionalnumberdetail_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='additionaldatedetail',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='additionalnumberdetail',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='additionaltextdetail',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='additionaldatedetail',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.customdatefield'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additionalnumberdetail',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.customnumberfield'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='additionaltextdetail',
            name='field',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='company.customtextfield'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='additionaldatedetail',
            unique_together={('detail', 'field', 'effective_date')},
        ),
        migrations.AlterUniqueTogether(
            name='additionalnumberdetail',
            unique_together={('detail', 'field', 'effective_date')},
        ),
        migrations.AlterUniqueTogether(
            name='additionaltextdetail',
            unique_together={('detail', 'field', 'effective_date')},
        ),
    ]
