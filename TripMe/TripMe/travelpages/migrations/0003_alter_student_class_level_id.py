# Generated by Django 3.2.8 on 2021-11-15 23:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travelpages', '0002_rename_class_level_student_class_level_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='class_level_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='travelpages.grade_level', to_field='class_level'),
        ),
    ]
