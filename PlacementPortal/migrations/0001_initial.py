# Generated by Django 2.0.5 on 2018-07-05 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=10)),
                ('address', models.TextField()),
                ('guardian_parent_name', models.CharField(max_length=80)),
                ('guardian_parent_contact', models.CharField(max_length=10)),
                ('guardian_parent_profession', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('acronym', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_code', models.CharField(max_length=15)),
                ('subject_name', models.CharField(max_length=100)),
                ('internal_marks', models.IntegerField()),
                ('external_marks', models.IntegerField()),
                ('total_marks', models.IntegerField()),
                ('result', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('full_name', models.CharField(max_length=100)),
                ('date_of_birth', models.DateField()),
                ('hall_ticket_number', models.CharField(max_length=100, unique=True)),
                ('gender', models.BooleanField()),
                ('caste', models.CharField(max_length=100)),
                ('career_goal', models.TextField()),
                ('tenth_marks', models.IntegerField()),
                ('inter_marks', models.IntegerField()),
                ('btech_marks', models.IntegerField(default=-1)),
                ('backlogs', models.IntegerField(default=-1)),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlacementPortal.Contact')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlacementPortal.Department')),
            ],
        ),
        migrations.AddField(
            model_name='marks',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PlacementPortal.Student'),
        ),
    ]
