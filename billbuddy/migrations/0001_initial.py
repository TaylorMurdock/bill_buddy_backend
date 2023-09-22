# Generated by Django 4.2.5 on 2023-09-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_subscription', models.CharField(max_length=100)),
                ('subscription_image_url', models.CharField(max_length=100)),
                ('bill_date', models.DateField()),
                ('subscription_price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
