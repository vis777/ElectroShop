# Generated by Django 4.2.5 on 2023-10-14 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Frontapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterDb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Mobile_Number', models.IntegerField(blank=True, null=True)),
                ('Email', models.CharField(blank=True, max_length=100, null=True)),
                ('UserName', models.CharField(blank=True, max_length=100, null=True)),
                ('PassWord', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
