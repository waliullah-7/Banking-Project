# Generated by Django 4.2.5 on 2024-01-04 13:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BankModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankname', models.CharField(max_length=100)),
                ('swift_code', models.CharField(max_length=100)),
                ('inst_num', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BranchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('transit_num', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.EmailField(default='admin@enigmatix.io', max_length=254)),
                ('capacity', models.IntegerField(null=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='banks.bankmodel')),
            ],
        ),
    ]
