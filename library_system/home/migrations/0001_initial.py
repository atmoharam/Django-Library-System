# Generated by Django 3.2.5 on 2021-07-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=16)),
                ('author', models.CharField(max_length=20)),
                ('category', models.CharField(max_length=15)),
                ('availabilty', models.BooleanField(default=True)),
            ],
        ),
    ]
