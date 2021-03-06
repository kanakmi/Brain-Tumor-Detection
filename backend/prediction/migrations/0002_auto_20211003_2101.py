# Generated by Django 3.2.7 on 2021-10-03 15:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tumordata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom', models.CharField(max_length=100)),
                ('probability', models.CharField(max_length=80)),
                ('image', models.CharField(max_length=700)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='model_image',
        ),
    ]
