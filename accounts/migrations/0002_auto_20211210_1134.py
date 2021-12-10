# Generated by Django 2.2.24 on 2021-12-10 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='description',
            field=models.TextField(blank=True, default='', verbose_name='自己紹介'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='プロフィール画像'),
        ),
    ]