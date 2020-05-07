# Generated by Django 3.0.6 on 2020-05-06 20:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cohort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'cohort',
                'verbose_name_plural': 'cohorts',
            },
        ),
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('language', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'exercise',
                'verbose_name_plural': 'exercises',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('slack_handle', models.CharField(max_length=50)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuexapp.Cohort')),
            ],
            options={
                'verbose_name': 'student',
                'verbose_name_plural': 'students',
            },
        ),
        migrations.CreateModel(
            name='StudentExercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuexapp.Exercise')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuexapp.Student')),
            ],
            options={
                'verbose_name': 'student_exercise',
                'verbose_name_plural': 'student_exercises',
            },
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('slack_handle', models.CharField(max_length=50)),
                ('specialty', models.CharField(max_length=50)),
                ('cohort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stuexapp.Cohort')),
            ],
            options={
                'verbose_name': 'instructor',
                'verbose_name_plural': 'instructors',
            },
        ),
    ]
