# Generated by Django 4.0.4 on 2022-07-26 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0015_alter_register_doctor_user_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_doctor',
            name='user_type',
            field=models.CharField(choices=[('doctor', 'doctor'), ('patient', 'patient')], max_length=10),
        ),
    ]
