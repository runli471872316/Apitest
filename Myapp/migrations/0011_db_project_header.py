# Generated by Django 3.2.3 on 2021-05-27 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0010_db_step_mock_res'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_project_header',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_id', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=20, null=True)),
                ('key', models.CharField(max_length=20, null=True)),
                ('value', models.TextField(null=True)),
            ],
        ),
    ]
