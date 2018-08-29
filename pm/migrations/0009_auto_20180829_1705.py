# Generated by Django 2.0.8 on 2018-08-29 17:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pm', '0008_sample_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='sequence',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='创建时间'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sequence',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sequence_created', to=settings.AUTH_USER_MODEL, verbose_name='created by'),
        ),
        migrations.AddField(
            model_name='sequence',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='description'),
        ),
        migrations.AddField(
            model_name='sequence',
            name='last_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='上次修改'),
        ),
    ]
