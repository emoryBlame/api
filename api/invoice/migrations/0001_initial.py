# Generated by Django 2.2 on 2019-04-09 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('status', models.CharField(max_length=50)),
                ('price_currency', models.CharField(max_length=10)),
                ('price_amount', models.DecimalField(decimal_places=2, max_digits=20000)),
                ('receive_currency', models.CharField(blank=True, max_length=10)),
                ('receive_amount', models.CharField(blank=True, max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('order_id', models.IntegerField()),
                ('payment_url', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
                ('message', models.CharField(blank=True, max_length=200)),
                ('reason', models.CharField(blank=True, max_length=200)),
                ('errors', models.CharField(blank=True, max_length=2000)),
            ],
        ),
    ]