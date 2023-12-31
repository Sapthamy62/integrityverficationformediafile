# Generated by Django 4.1.7 on 2023-05-04 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Actors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(blank=True, max_length=255)),
                ('lastname', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
                ('status', models.CharField(blank=True, max_length=255)),
                ('Typeid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='welcome.usertype')),
            ],
        ),
    ]
