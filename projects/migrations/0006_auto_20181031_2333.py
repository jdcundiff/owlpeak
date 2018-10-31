# Generated by Django 2.1.2 on 2018-10-31 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20181031_2312'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='ongoing',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='project',
            name='ended_at',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='started_at',
            field=models.DateField(null=True),
        ),
    ]
