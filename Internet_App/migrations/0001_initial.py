# Generated by Django 5.0.1 on 2024-02-08 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signupmaster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(max_length=30)),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('gmail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=12)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('mobile', models.BigIntegerField()),
            ],
        ),
    ]
