# Generated by Django 2.0.3 on 2018-05-21 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApps', '0002_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='description',
            field=models.CharField(default='No Description', max_length=1000),
        ),
    ]
