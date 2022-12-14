# Generated by Django 4.0.6 on 2022-08-03 07:37

from django.conf import settings
from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('group', models.PositiveIntegerField(blank=True, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('course', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('author', models.ManyToManyField(related_name='student', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('degree', models.CharField(choices=[('MASTER', 'Master'), ('SENIOR', 'Senior'), ('MIDDLE', 'Middle'), ('JUNIOR', 'Junior'), ('MAGISTR', 'Magistr'), ('PHD_CANDIDANT', 'PhD_Candidant'), ('DOTSENT', 'Dotsent')], default='MASTER', max_length=15)),
                ('author', models.ManyToManyField(related_name='teacher', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'teacher',
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
                ('module', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('students', models.ManyToManyField(to='course.student')),
                ('teachers', models.ManyToManyField(to='course.teacher')),
            ],
            options={
                'db_table': 'subject',
            },
        ),
    ]
