# Generated by Django 5.0 on 2024-07-07 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proje', '0002_rename_üstyazi_mansets_ustyazi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('baslik', models.CharField(max_length=100)),
                ('blog', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='sample')),
            ],
        ),
    ]
