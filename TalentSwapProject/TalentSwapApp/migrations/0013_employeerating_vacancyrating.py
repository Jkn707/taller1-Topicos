# Generated by Django 5.0.2 on 2024-04-25 09:49

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TalentSwapApp', '0012_alter_application_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='TalentSwapApp.employee')),
            ],
        ),
        migrations.CreateModel(
            name='VacancyRating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('experience', models.CharField(default=' No comments', max_length=300)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='TalentSwapApp.vacancy')),
            ],
        ),
    ]
