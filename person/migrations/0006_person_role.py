# Generated by Django 4.2 on 2023-11-29 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_alter_skill_scale'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='role',
            field=models.CharField(max_length=50, null=True),
        ),
    ]