# Generated by Django 4.2.4 on 2023-08-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_register'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('logo', models.ImageField(upload_to='logo')),
            ],
        ),
    ]