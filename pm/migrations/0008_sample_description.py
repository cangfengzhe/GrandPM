# Generated by Django 2.0.8 on 2018-08-29 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0007_auto_20180829_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='sample',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='description'),
        ),
    ]
