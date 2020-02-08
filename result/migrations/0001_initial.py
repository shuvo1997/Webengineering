# Generated by Django 3.0.2 on 2020-01-22 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0004_auto_20200123_0130'),
    ]

    operations = [
        migrations.CreateModel(
            name='payment',
            fields=[
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='application.Applicant_new')),
                ('transaction_id', models.CharField(max_length=10, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='admission_result',
            fields=[
                ('applicant', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='result.payment')),
                ('bangla_marks', models.IntegerField()),
                ('english_marks', models.IntegerField()),
                ('math_marks', models.IntegerField()),
            ],
        ),
    ]