# Generated by Django 4.1.9 on 2023-06-09 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Backend', '0015_problemtag_problemtag_unique_problem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('creationTimeSeconds', models.DateTimeField(auto_now_add=True)),
                ('relativeTimeSeconds', models.IntegerField()),
                ('programmingLanguage', models.CharField(max_length=255)),
                ('verdict', models.CharField(choices=[('FAILED', 'FAILED'), ('OK', 'OK'), ('PARTIAL', 'PARTIAL'), ('COMPILATION_ERROR', 'COMPILATION_ERROR'), ('RUNTIME_ERROR', 'RUNTIME_ERROR'), ('WRONG_ANSWER', 'WRONG_ANSWER'), ('PRESENTATION_ERROR', 'PRESENTATION_ERROR'), ('TIME_LIMIT_EXCEEDED', 'TIME_LIMIT_EXCEEDED'), ('MEMORY_LIMIT_EXCEEDED', 'MEMORY_LIMIT_EXCEEDED'), ('IDLENESS_LIMIT_EXCEEDED', 'IDLENESS_LIMIT_EXCEEDED'), ('SECURITY_VIOLATED', 'SECURITY_VIOLATED'), ('CRASHED', 'CRASHED'), ('INPUT_PREPARATION_CRASHED', 'INPUT_PREPARATION_CRASHED'), ('CHALLENGED', 'CHALLENGED'), ('SKIPPED', 'SKIPPED'), ('TESTING', 'TESTING'), ('REJECTED', 'REJECTED')], max_length=100, null=True)),
                ('testset', models.CharField(choices=[('SAMPLES', 'SAMPLES'), ('PRETESTS', 'PRETESTS'), ('TESTS', 'TESTS'), ('CHALLENGES', 'CHALLENGES'), ('TESTS1', 'TESTS1'), ('TESTS2', 'TESTS2'), ('TESTS3', 'TESTS3'), ('TESTS4', 'TESTS4'), ('TESTS5', 'TESTS5'), ('TESTS6', 'TESTS6'), ('TESTS7', 'TESTS7'), ('TESTS8', 'TESTS8'), ('TESTS9', 'TESTS9'), ('TESTS10', 'TESTS10')], max_length=10, null=True)),
                ('passedTestCount', models.IntegerField()),
                ('timeConsumedMillis', models.IntegerField()),
                ('memoryConsumedBytes', models.IntegerField()),
                ('points', models.FloatField(null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submissions', to='Backend.partymember')),
                ('contestId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_submissions', to='Backend.problem')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='problem_submissions_with_index', to='Backend.problem')),
            ],
            options={
                'verbose_name': 'Problem Submission',
                'verbose_name_plural': 'Problem Submissions',
            },
        ),
    ]