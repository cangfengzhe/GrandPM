# Generated by Django 2.0.8 on 2018-08-29 16:06

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('pm', '0004_auto_20180829_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='custom',
            name='tel',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='客户电话'),
        ),
        migrations.AlterField(
            model_name='project',
            name='analysis_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('甲基化', '甲基化'), ('结构变异', '结构变异'), ('肿瘤', '肿瘤')], default='sv', max_length=20, verbose_name='analysis_type'),
        ),
    ]