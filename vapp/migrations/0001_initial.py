# Generated by Django 4.0.3 on 2022-03-22 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module_name', models.CharField(max_length=64)),
                ('module_code', models.CharField(max_length=16)),
                ('year', models.IntegerField(choices=[(2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023), (2024, 2024), (2025, 2025)])),
                ('semester', models.IntegerField(choices=[(1, 1), (2, 2)])),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('professor_id', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('student_id', models.CharField(max_length=64)),
                ('module', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='vapp.module')),
                ('professor', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='vapp.professor')),
            ],
        ),
        migrations.AddField(
            model_name='module',
            name='professors',
            field=models.ManyToManyField(blank=True, to='vapp.professor'),
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.UniqueConstraint(fields=('professor', 'module', 'student_id'), name='unique_rating'),
        ),
        migrations.AddConstraint(
            model_name='module',
            constraint=models.UniqueConstraint(fields=('module_name', 'module_code', 'year', 'semester'), name='unique_module_instance'),
        ),
    ]