# Generated by Django 2.1.1 on 2018-12-12 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_otherpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='otherpage',
            name='intro',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
