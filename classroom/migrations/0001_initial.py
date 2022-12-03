# Generated by Django 3.0.3 on 2022-12-02 16:48

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
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('invitation_code', models.CharField(blank=True, max_length=15)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='created_classes', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(related_name='joined_classes', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
    ]