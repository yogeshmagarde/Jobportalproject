# Generated by Django 4.0.2 on 2022-06-07 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0010_resume_univercity'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='dunivercity',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='gunivercity',
            field=models.CharField(default=' ', max_length=50),
        ),
        migrations.AddField(
            model_name='resume',
            name='pgunivercity',
            field=models.CharField(default=' ', max_length=50),
        ),
    ]
