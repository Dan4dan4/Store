# Generated by Django 4.2.19 on 2025-03-04 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('material', models.CharField(max_length=200)),
            ],
        ),
    ]
