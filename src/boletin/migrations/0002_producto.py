# Generated by Django 2.2.7 on 2020-01-07 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boletin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
