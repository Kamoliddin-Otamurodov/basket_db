# Generated by Django 5.0 on 2024-03-17 07:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coaches', to='player.city')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='player.city')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('surname', models.CharField(max_length=128)),
                ('born_date', models.DateTimeField()),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('position', models.CharField(choices=[('PG', 'Piont Guard'), ('SG', 'Shooting Guard'), ('SF', 'Small Forward'), ('PF', 'Power Forward'), ('C', 'Center')], max_length=20, unique=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='player.city')),
                ('coach', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='player.coach')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='player.team')),
            ],
        ),
        migrations.AddField(
            model_name='coach',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='player.team'),
        ),
    ]
