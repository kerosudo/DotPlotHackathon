# Generated by Django 5.0.7 on 2024-07-24 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DotPlot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usscans',
            name='patient',
        ),
        migrations.AddField(
            model_name='patients',
            name='scanID',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usscans',
            name='scanID',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
