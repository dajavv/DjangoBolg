# Generated by Django 4.2.3 on 2023-07-17 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_adminuser_alter_post_photos'),
    ]

    operations = [
        migrations.RenameField(
            model_name='adminuser',
            old_name='name',
            new_name='aname',
        ),
    ]
