# Generated by Django 4.2.7 on 2023-12-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemdemenu',
            name='foto',
            field=models.CharField(default='nome padrao', max_length=100),
        ),
    ]
