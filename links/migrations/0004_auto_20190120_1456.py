# Generated by Django 2.0.10 on 2019-01-20 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_link_taglist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='taglist',
            field=models.CharField(max_length=1000),
        ),
    ]
