# Generated by Django 2.2.7 on 2019-11-21 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=8)),
                ('comp_id', models.IntegerField()),
                ('tel', models.IntegerField()),
                ('username', models.CharField(max_length=30)),
            ],
        ),
    ]
