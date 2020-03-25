# Generated by Django 3.0.3 on 2020-03-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shoecolor',
            name='color',
            field=models.CharField(choices=[('RED', 'Red'), ('ORANGE', 'Orange'), ('YELLOW', 'Yellow'), ('GREEN', 'Green'), ('BLUE', 'Blue'), ('INDIGO', 'Indigo'), ('VIOLET', 'Violet'), ('BLACK', 'Black'), ('WHITE', 'White')], default='RED', max_length=10),
        ),
    ]