# Generated by Django 2.0.5 on 2019-02-04 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0003_mate'),
    ]

    operations = [
        migrations.AddField(
            model_name='mate',
            name='name',
            field=models.CharField(default='straanger', max_length=2000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='mate',
            name='mobno',
            field=models.CharField(max_length=10),
        ),
    ]
