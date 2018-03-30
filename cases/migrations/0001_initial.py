# Generated by Django 2.0.3 on 2018-03-30 04:22

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=30)),
                ('client_email', models.EmailField(default='', max_length=254)),
                ('client_phone', phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128)),
                ('client_SID', models.CharField(default='', max_length=10)),
                ('incident_description', models.TextField(default='')),
                ('open_date', models.DateField(auto_now_add=True, verbose_name='Date case was opened')),
                ('close_date', models.DateField(blank=True, verbose_name='Date case was closed')),
                ('division', models.CharField(choices=[('ACA', 'Academic'), ('GRI', 'Grievance'), ('FIN', 'Financial Aid'), ('CON', 'Conduct')], default='ACA', max_length=3)),
                ('isOpen', models.BooleanField(default=True, verbose_name='Case open?')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('division', models.CharField(choices=[('ACA', 'Academic'), ('GRI', 'Grievance'), ('FIN', 'Financial Aid'), ('CON', 'Conduct')], default='ACA', max_length=3)),
                ('name', models.CharField(max_length=30)),
                ('slug', models.SlugField(default='', max_length=30)),
            ],
            options={
                'verbose_name': 'Caseworker',
            },
        ),
        migrations.AddField(
            model_name='case',
            name='caseworker',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cases.Person'),
        ),
    ]
