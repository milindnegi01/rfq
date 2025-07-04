# Generated by Django 4.2.21 on 2025-05-27 11:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('client_admin', 'Client Admin'), ('end_user', 'End User'), ('supplier', 'Supplier')], max_length=20),
        ),
        migrations.CreateModel(
            name='ClientAdminProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_id', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255)),
                ('client_org_address', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='client_admin_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
