# Generated by Django 4.2.6 on 2023-10-11 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_news_news_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_img',
            field=models.FileField(default=None, null=True, upload_to='media/'),
        ),
    ]