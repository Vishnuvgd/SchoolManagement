# Generated by Django 5.1.2 on 2024-10-23 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_app', '0009_librarymodel_book_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feesmodel',
            name='payment_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
