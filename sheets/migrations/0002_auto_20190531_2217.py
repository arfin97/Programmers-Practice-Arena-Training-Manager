# Generated by Django 2.1.3 on 2019-05-31 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sheets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sheet',
            name='cut_off',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]