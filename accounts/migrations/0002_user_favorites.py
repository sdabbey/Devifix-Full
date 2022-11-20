# Generated by Django 4.1.3 on 2022-11-14 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorites',
            field=models.ManyToManyField(blank=True, null=True, related_name='saved_by', to='orders.order'),
        ),
    ]