# Generated by Django 2.0.2 on 2018-08-21 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20180820_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='RunDdos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Domain名称')),
            ],
            options={
                'verbose_name': '创建ddos防护服务',
                'verbose_name_plural': '创建ddos防护服务',
            },
        ),
    ]
