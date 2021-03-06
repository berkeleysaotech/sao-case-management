# Generated by Django 2.1.5 on 2019-12-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cases', '0008_case_client_pronouns'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='semester_food',
            field=models.BooleanField(default=True, verbose_name='Do you have enough food for the duration of the semester?'),
        ),
        migrations.AddField(
            model_name='case',
            name='week_food',
            field=models.BooleanField(default=True, verbose_name='Do you have enough food for the week?'),
        ),
        migrations.AddField(
            model_name='case',
            name='week_housing',
            field=models.BooleanField(default=True, verbose_name='Do you have a safe and stable home for tonight and the rest of this week?'),
        ),
    ]
