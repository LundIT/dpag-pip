# Generated by Django 4.0.4 on 2024-01-05 16:23

import ProcessAdminRestApi.models.fields.XLSX_field
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CalculationLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('timestamp', models.DateTimeField()),
                ('trigger_name', models.TextField(null=True)),
                ('message_type', models.TextField(default='')),
                ('calculationId', models.TextField(default='test_id')),
                ('message', models.TextField()),
                ('method', models.TextField()),
                ('is_notification', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('group', models.TextField(null=True)),
                ('logfile', ProcessAdminRestApi.models.fields.XLSX_field.XLSXField(default='', max_length=300, upload_to='')),
                ('input_validation', ProcessAdminRestApi.models.fields.XLSX_field.XLSXField(default='', max_length=300, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='UserChangeLog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('message', models.TextField()),
                ('traceback', models.TextField(default='', null=True)),
                ('calculationId', models.TextField(default='-1')),
            ],
        ),
        migrations.AddConstraint(
            model_name='log',
            constraint=models.UniqueConstraint(fields=('group',), name='defining_fields_Log'),
        ),
    ]