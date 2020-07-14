# Generated by Django 3.0.8 on 2020-07-14 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('course', models.CharField(max_length=140)),
                ('rating', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
