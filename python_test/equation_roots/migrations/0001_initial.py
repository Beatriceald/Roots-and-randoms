# Generated by Django 4.0.4 on 2022-06-10 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EquationValues',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.IntegerField()),
                ('b', models.IntegerField()),
                ('c', models.IntegerField()),
            ],
        ),
    ]
