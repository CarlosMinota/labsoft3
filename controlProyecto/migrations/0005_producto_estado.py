# Generated by Django 2.2.5 on 2022-05-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('controlProyecto', '0004_auto_20220512_1112'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
