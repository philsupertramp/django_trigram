# Generated by Django 2.2.1 on 2019-05-13 10:50
from django.contrib.postgres.operations import TrigramExtension
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trigram', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ModelC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='trigram.ModelA')),
                ('b', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='trigram.ModelB')),
            ],
        ),
        TrigramExtension()
    ]
