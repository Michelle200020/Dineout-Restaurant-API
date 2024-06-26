# Generated by Django 5.0.2 on 2024-05-03 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('restaurant_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('cuisines', models.JSONField()),
                ('price', models.IntegerField()),
                ('location', models.CharField(max_length=100)),
                ('open_from', models.CharField(max_length=8)),
                ('open_till', models.CharField(max_length=8)),
                ('offer', models.CharField(max_length=20)),
                ('offer_type', models.CharField(max_length=20)),
                ('restaurant_type', models.CharField(max_length=100)),
                ('features', models.JSONField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=3)),
                ('votes', models.CharField(max_length=20)),
                ('reviews', models.CharField(max_length=20)),
                ('outlet_count', models.IntegerField()),
            ],
        ),
    ]
