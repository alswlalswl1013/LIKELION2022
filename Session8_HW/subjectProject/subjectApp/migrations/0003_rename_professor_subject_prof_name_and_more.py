# Generated by Django 4.0.3 on 2022-04-07 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subjectApp', '0002_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='professor',
            new_name='prof_name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='title',
            new_name='subject_name',
        ),
    ]
