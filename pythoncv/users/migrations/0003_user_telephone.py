# Generated by Django 4.2.3 on 2023-07-28 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_birthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='telephone',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Telephone'),
        ),
    ]
