# Generated by Django 3.0.2 on 2020-01-08 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_auto_20200106_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicant_new',
            name='admission_class',
            field=models.IntegerField(default='0'),
        ),
    ]
