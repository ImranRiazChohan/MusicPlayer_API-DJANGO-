# Generated by Django 3.1.5 on 2021-03-05 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SongModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name_of_the_Song', models.CharField(max_length=100)),
                ('time_Duration', models.IntegerField()),
                ('Upload_time', models.DateTimeField(verbose_name='Published_data : ')),
            ],
        ),
    ]