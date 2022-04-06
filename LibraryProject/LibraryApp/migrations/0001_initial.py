# Generated by Django 4.0.3 on 2022-04-04 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_Name', models.CharField(max_length=100)),
                ('Description', models.TextField(blank=True)),
                ('Language', models.CharField(max_length=100)),
                ('Book_Author', models.CharField(max_length=100)),
            ],
        ),
    ]
