# Generated by Django 3.1.3 on 2021-03-22 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='picture',
            name='material',
            field=models.ManyToManyField(to='main.Material'),
        ),
        migrations.DeleteModel(
            name='PicMat',
        ),
    ]
