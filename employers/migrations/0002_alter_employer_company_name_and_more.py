# Generated by Django 5.2.1 on 2025-05-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employer',
            name='company_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='employer',
            name='contact_person_name',
            field=models.CharField(max_length=255),
        ),
    ]
