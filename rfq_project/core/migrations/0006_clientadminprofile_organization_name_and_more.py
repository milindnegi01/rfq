# Generated by Django 4.2.21 on 2025-06-04 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='clientadminprofile',
            name='organization_name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='enduserprofile',
            name='organization_name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
