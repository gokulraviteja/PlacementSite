# Generated by Django 2.0.5 on 2019-02-03 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=2000)),
                ('branch', models.CharField(max_length=2000)),
                ('comcount', models.IntegerField(default=0)),
            ],
        ),
    ]