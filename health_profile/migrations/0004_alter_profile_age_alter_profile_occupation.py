# Generated by Django 5.1 on 2024-09-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health_profile', '0003_alter_profile_age_alter_profile_avg_screen_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='occupation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]