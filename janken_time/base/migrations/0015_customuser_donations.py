# Generated by Django 4.0 on 2022-03-27 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_alter_customuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='donations',
            field=models.IntegerField(default=0, verbose_name='寄付額'),
        ),
    ]
