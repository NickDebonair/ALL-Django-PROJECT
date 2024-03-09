# Generated by Django 4.0 on 2022-03-20 04:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_category_alter_champion_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='champion',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='base.category', verbose_name='Category'),
            preserve_default=False,
        ),
    ]
