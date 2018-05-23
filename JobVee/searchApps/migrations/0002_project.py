# Generated by Django 2.0.3 on 2018-05-20 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchApps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=20)),
                ('deadline', models.DateField()),
                ('wage', models.IntegerField()),
                ('description', models.CharField(default='', max_length=1000)),
            ],
        ),
    ]