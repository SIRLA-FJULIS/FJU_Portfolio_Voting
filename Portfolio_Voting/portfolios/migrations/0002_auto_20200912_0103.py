# Generated by Django 3.0.6 on 2020-09-11 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work',
            name='work_college',
            field=models.CharField(choices=[('文學院', '文學院'), ('藝術學院', '藝術學院'), ('傳播學院', '傳播學院'), ('教育學院', '教育學院'), ('醫學院', '醫學院'), ('理工學院', '理工學院'), ('外國語文學院', '外國語文學院'), ('民生學院', '民生學院'), ('法律學院', '法律學院'), ('社會科學院', '社會科學院'), ('管理學院', '管理學院'), ('織品服裝學院', '織品服裝學院'), ('全人專班-僑生國文', '全人專班-僑生國文')], max_length=50),
        ),
    ]
