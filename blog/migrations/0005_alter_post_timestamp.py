# Generated by Django 3.2 on 2021-05-02 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='timeStamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]