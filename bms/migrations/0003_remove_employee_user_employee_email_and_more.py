# Generated by Django 5.1.5 on 2025-01-23 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bms', '0002_remove_employee_email_remove_employee_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='user',
        ),
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='メールアドレス'),
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='名'),
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='姓'),
        ),
    ]
