# Generated by Django 4.2.2 on 2024-03-11 02:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hibiLaboSystem', '0030_selfcheckindustry_selfcheckrole_remove_user_role_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': 'Roles', 'verbose_name_plural': 'Roles'},
        ),
        migrations.AlterModelOptions(
            name='selfcheckindustry',
            options={'verbose_name': 'Selfcheck Industries', 'verbose_name_plural': 'Selfcheck Industries'},
        ),
        migrations.AlterModelOptions(
            name='selfcheckrole',
            options={'verbose_name': 'Selfcheck Roles', 'verbose_name_plural': 'Selfcheck Roles'},
        ),
        migrations.AlterModelTable(
            name='role',
            table='roles',
        ),
        migrations.AlterModelTable(
            name='selfcheckindustry',
            table='selfcheck_industries',
        ),
        migrations.AlterModelTable(
            name='selfcheckrole',
            table='selfcheck_roles',
        ),
    ]