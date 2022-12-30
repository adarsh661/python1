# Generated by Django 3.2.16 on 2022-10-24 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='team')),
                ('name', models.CharField(max_length=250)),
                ('description', models.TextField()),
            ],
        ),
    ]
