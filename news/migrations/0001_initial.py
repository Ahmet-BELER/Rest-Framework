# Generated by Django 4.1.1 on 2022-10-02 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=100)),
                ('header', models.CharField(max_length=100)),
                ('explanation', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('city', models.CharField(max_length=100)),
                ('release_date', models.DateField()),
                ('active', models.BooleanField(default=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('update_date', models.DateField(auto_now=True)),
            ],
        ),
    ]
