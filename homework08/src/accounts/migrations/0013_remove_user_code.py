# Generated by Django 2.0.1 on 2020-05-26 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20200526_1643'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='code',
        ),
    ]