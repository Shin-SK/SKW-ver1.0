# Generated by Django 5.1.5 on 2025-02-21 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docspdf', '0009_quotation_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='deadline',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='納期'),
        ),
    ]
