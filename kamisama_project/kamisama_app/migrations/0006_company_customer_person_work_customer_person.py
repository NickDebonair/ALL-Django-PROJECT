# Generated by Django 4.0 on 2022-04-03 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kamisama_app', '0005_rename_category1_kamisama_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_type', models.IntegerField(choices=[(0, '法人'), (1, '個人')])),
                ('company', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.company')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.customer')),
            ],
        ),
        migrations.AddField(
            model_name='customer',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.person'),
        ),
    ]
