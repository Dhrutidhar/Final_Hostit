# Generated by Django 5.0.1 on 2024-02-20 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Internet_App', '0006_admin_signupmaster_delete_signupmaster_adm'),
    ]

    operations = [
        migrations.CreateModel(
            name='complain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mob', models.BigIntegerField()),
                ('complain_type', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
            ],
        ),
    ]
