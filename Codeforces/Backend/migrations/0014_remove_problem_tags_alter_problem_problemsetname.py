# Generated by Django 4.1.9 on 2023-06-09 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0013_member_party_partymember_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='problem',
            name='tags',
        ),
        migrations.AlterField(
            model_name='problem',
            name='problemsetName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
