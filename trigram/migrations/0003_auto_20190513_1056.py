# Generated by Django 2.2.1 on 2019-05-13 10:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trigram', '0002_modelc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelc',
            name='a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trigram.ModelA'),
        ),
        migrations.AlterField(
            model_name='modelc',
            name='b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='trigram.ModelB'),
        ),
    ]