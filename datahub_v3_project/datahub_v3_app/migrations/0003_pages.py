# Generated by Django 4.1.1 on 2022-11-08 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahub_v3_app', '0002_schedule_log'),
    ]

    operations = [
        migrations.CreateModel(
            name='pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_name', models.CharField(max_length=300)),
                ('module_name', models.CharField(max_length=300, null=True)),
                ('page_url', models.URLField()),
                ('start_date', models.DateField(auto_now=True)),
                ('end_date', models.DateField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.CharField(max_length=300, null=True)),
                ('created_on', models.CharField(max_length=300, null=True)),
            ],
            options={
                'db_table': 'pages',
            },
        ),
    ]