# Generated by Django 3.1.3 on 2021-05-12 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myapp', '0004_db_apis'),
    ]

    operations = [
        migrations.AddField(
            model_name='db_apis',
            name='last_api_body',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='db_apis',
            name='last_body_method',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
