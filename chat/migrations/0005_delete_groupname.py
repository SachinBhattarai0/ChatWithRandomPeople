# Generated by Django 3.2.10 on 2022-02-15 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_alter_groupname_groupname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='groupName',
        ),
    ]
