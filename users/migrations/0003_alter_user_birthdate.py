# Generated by Django 4.2 on 2023-04-17 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_rename_is_employe_user_is_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birthdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]