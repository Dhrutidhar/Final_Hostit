# Generated by Django 5.0.1 on 2024-03-07 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internet_App', '0012_rename_admin_signupmaster_signupmaster'),
    ]

    operations = [
        migrations.CreateModel(
            name='subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
