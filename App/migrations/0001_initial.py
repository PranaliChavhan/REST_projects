# Generated by Django 3.0 on 2022-02-19 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Auther', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='books/pdf/')),
                ('cover', models.ImageField(blank=True, null=True, upload_to='books/covers/')),
            ],
        ),
    ]