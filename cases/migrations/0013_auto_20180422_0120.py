# Generated by Django 2.0.4 on 2018-04-22 08:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0012_auto_20180422_0042'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='caseupdate',
            options={'ordering': ['-creation_date']},
        ),
    ]
