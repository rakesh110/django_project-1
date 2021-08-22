# Generated by Django 3.1.7 on 2021-03-17 05:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_no', models.IntegerField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('employee_name', models.CharField(max_length=80)),
                ('father_name', models.CharField(max_length=80)),
                ('gender', models.CharField(max_length=100)),
                ('residence', models.CharField(max_length=200)),
                ('dob', models.DateField()),
                ('physical_fitness', models.CharField(max_length=200)),
                ('descriptive_marks', models.CharField(max_length=100)),
                ('refusel_of_certificate', models.CharField(max_length=80)),
                ('certificate_being_revoked', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('telephone', models.PositiveIntegerField()),
                ('email', models.CharField(max_length=50, null=True)),
                ('factory', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('examination_after_a_period', models.IntegerField(blank=True)),
            ],
        ),
    ]
