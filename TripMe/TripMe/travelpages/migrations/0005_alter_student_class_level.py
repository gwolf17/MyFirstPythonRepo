# Generated by Django 3.2.8 on 2021-11-16 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelpages', '0004_rename_class_level_id_student_class_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_level',
            field=models.CharField(blank=True, choices=[('FR', 'FRESHMAN'), ('SO', 'SOPHOMORE'), ('JR', 'JUNIOR'), ('SR', 'SENIOR')], max_length=2, null=True),
        ),
    ]
