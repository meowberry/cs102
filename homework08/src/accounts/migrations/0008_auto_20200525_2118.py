# Generated by Django 2.0.1 on 2020-05-25 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200525_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='code',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
    ]
