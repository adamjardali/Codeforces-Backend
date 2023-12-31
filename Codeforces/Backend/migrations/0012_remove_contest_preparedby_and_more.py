# Generated by Django 4.1.9 on 2023-06-09 07:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0011_alter_comment_options_remove_blogentry_tags_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contest',
            name='preparedBy',
        ),
        migrations.AlterField(
            model_name='ratingchange',
            name='contestName',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='recentaction',
            name='blogEntryId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backend.blogentry'),
        ),
        migrations.AlterField(
            model_name='recentaction',
            name='commentId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backend.comment'),
        ),
        migrations.CreateModel(
            name='ContestAuthors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authorHandle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backend.codeforcesuser')),
                ('contestId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Backend.contest')),
            ],
            options={
                'verbose_name': 'Contest Author',
                'verbose_name_plural': 'Contest Authors',
            },
        ),
        migrations.AddConstraint(
            model_name='contestauthors',
            constraint=models.UniqueConstraint(fields=('contestId', 'authorHandle'), name='unique_contest_author'),
        ),
    ]
