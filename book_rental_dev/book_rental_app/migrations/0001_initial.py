# Generated by Django 3.2 on 2022-06-23 01:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manage_id', models.IntegerField(blank=True, null=True, verbose_name='書籍管理用ID')),
                ('id_in_category', models.IntegerField(blank=True, null=True, verbose_name='カテゴリーにおけるID')),
                ('title', models.CharField(max_length=255, verbose_name='Book Title')),
                ('is_rental', models.BooleanField(default=False, help_text='借りられたらTrue', verbose_name='貸出中ラベル')),
                ('borrower_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='borrowing_book', to=settings.AUTH_USER_MODEL, verbose_name='本を借りた人')),
            ],
            options={
                'verbose_name': '書籍情報',
                'verbose_name_plural': '書籍情報',
                'db_table': 'Books',
            },
        ),
        migrations.CreateModel(
            name='LargeCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Large Categroy name')),
            ],
            options={
                'verbose_name': '大カテゴリー',
                'verbose_name_plural': '大カテゴリー',
                'db_table': 'Large_Category',
            },
        ),
        migrations.CreateModel(
            name='SmallCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, verbose_name='Small Categroy name')),
                ('large_category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_rental_app.largecategory', verbose_name='Large Categroy name')),
            ],
            options={
                'verbose_name': '小カテゴリー',
                'verbose_name_plural': '小カテゴリー',
                'db_table': 'Small_Category',
            },
        ),
        migrations.CreateModel(
            name='LendingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkout_date', models.DateTimeField(auto_now_add=True, verbose_name='貸し出し日')),
                ('due_date', models.DateField(verbose_name='返却予定日')),
                ('return_date', models.DateTimeField(auto_now=True, verbose_name='返却日')),
                ('is_returned', models.BooleanField(default=False, help_text='本が返されたらTrue', verbose_name='返されたかどうかのラベル')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='book_rental_app.books', verbose_name='貸し出された書籍')),
                ('borrower_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_borrower', to=settings.AUTH_USER_MODEL, verbose_name='本を借りた人')),
                ('lender_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status_lender', to=settings.AUTH_USER_MODEL, verbose_name='貸出許可を出した人')),
            ],
            options={
                'verbose_name': '貸出状況',
                'verbose_name_plural': '貸出状況',
                'db_table': 'LendingStatus',
            },
        ),
        migrations.AddField(
            model_name='books',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_rental_app.smallcategory', verbose_name='Small Categroy name'),
        ),
        migrations.AddField(
            model_name='books',
            name='lender_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lending_book', to=settings.AUTH_USER_MODEL, verbose_name='貸出許可を出した人'),
        ),
    ]