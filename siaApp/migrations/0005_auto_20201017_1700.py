# Generated by Django 3.1.2 on 2020-10-17 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siaApp', '0004_awardlist_award_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='awardlist',
            name='award_date',
            field=models.CharField(max_length=30),
        ),
    ]
