# Generated by Django 3.0.8 on 2020-07-16 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('types', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('result', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='philosophy.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=300)),
                ('date', models.DateField()),
                ('postid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='philosophy.Post')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='philosophy.User')),
            ],
        ),
    ]
