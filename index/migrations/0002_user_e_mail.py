# Generated by Django 2.2.2 on 2019-11-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='e_mail',
            field=models.CharField(default='abc@abc.com', max_length=128),
        ),
    ]
