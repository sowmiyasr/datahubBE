# Generated by Django 4.1.1 on 2022-10-18 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahub_v3_app', '0002_dumy_model_delete_company_register_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='pipiline_sche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pipeline_schedule_desc', models.CharField(max_length=100)),
                ('Pipeline_schedule_name', models.CharField(max_length=100)),
                ('pipeline_schedule_start_date', models.DateField()),
                ('pipeline_schedule_end_date', models.DateField()),
                ('pipeline_schedule_time', models.TimeField()),
                ('pipeline_schedule_run_imme', models.BooleanField()),
                ('pipeline_status', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'pipeline_sche',
            },
        ),
        migrations.DeleteModel(
            name='pipiline_schedule',
        ),
    ]
