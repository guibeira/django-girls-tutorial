# Generated by Django 2.2.10 on 2020-02-08 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.CharField(default=' teste lalala', max_length=200),
            preserve_default=False,
        ),
    ]
