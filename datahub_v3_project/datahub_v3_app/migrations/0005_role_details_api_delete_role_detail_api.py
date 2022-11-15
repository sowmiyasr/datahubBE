# Generated by Django 4.1.1 on 2022-11-15 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datahub_v3_app', '0004_user_role_view_delete_users_role_view'),
    ]

    operations = [
        migrations.CreateModel(
            name='role_details_api',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role_name', models.CharField(max_length=100)),
                ('role_detail_name', models.CharField(max_length=100)),
                ('role_description', models.CharField(max_length=150)),
                ('role_handling_pages', models.JSONField()),
                ('read', models.BooleanField(default=True)),
                ('write', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'role_details',
            },
        ),
        migrations.DeleteModel(
            name='role_detail_api',
        ),
    ]
