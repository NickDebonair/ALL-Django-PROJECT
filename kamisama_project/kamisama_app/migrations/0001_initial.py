# Generated by Django 4.0 on 2022-04-03 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mibunrui',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Mibunrui', max_length=20)),
            ],
            options={
                'verbose_name': '第三類型',
                'verbose_name_plural': '第三類型',
            },
        ),
        migrations.CreateModel(
            name='Narimasu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Narimasu', max_length=20)),
            ],
            options={
                'verbose_name': '第一類型',
                'verbose_name_plural': '第一類型',
            },
        ),
        migrations.CreateModel(
            name='Sonota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sonota', max_length=20)),
            ],
            options={
                'verbose_name': 'その他',
                'verbose_name_plural': 'その他',
            },
        ),
        migrations.CreateModel(
            name='Umareru',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Umareru', max_length=20)),
            ],
            options={
                'verbose_name': '第二類型',
                'verbose_name_plural': '第二類型',
            },
        ),
        migrations.CreateModel(
            name='ZoukeSanshin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.narimasu')),
            ],
            options={
                'verbose_name': '別天神',
                'verbose_name_plural': '別天神',
            },
        ),
        migrations.CreateModel(
            name='ShindaiNanadai',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.narimasu')),
            ],
            options={
                'verbose_name': '神代七代',
                'verbose_name_plural': '神代七代',
            },
        ),
        migrations.CreateModel(
            name='DaisangunNarimasu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Daisangun', max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.narimasu')),
            ],
            options={
                'verbose_name': '第三群',
                'verbose_name_plural': '第三群',
            },
        ),
        migrations.CreateModel(
            name='DaiichiNarimasu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kamisama_app.daisangunnarimasu')),
            ],
        ),
    ]