# Generated by Django 4.0.2 on 2022-03-15 10:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_pledge'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pledge',
            old_name='anonyous',
            new_name='anonymous',
        ),
    ]