# Generated by Django 3.2.8 on 2021-11-17 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelpages', '0007_rename_class_level_id_student_class_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_level',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.DO_NOTHING, to='travelpages.grade_level', to_field='class_level', verbose_name='student class'),
        ),
    ]