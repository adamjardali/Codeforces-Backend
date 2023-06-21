# Generated by Django 4.1.9 on 2023-06-09 08:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0014_remove_problem_tags_alter_problem_problemsetname'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProblemTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=255)),
                ('contestId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_tags', to='Backend.problem')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_tags_index', to='Backend.problem')),
            ],
            options={
                'db_table': 'problemtag',
            },
        ),
        migrations.AddConstraint(
            model_name='problemtag',
            constraint=models.UniqueConstraint(fields=('contestId', 'index', 'tag'), name='unique_problem_tag'),
        ),
    ]