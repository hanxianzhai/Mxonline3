# Generated by Django 2.0.2 on 2018-07-28 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_remove_userprofile_tuijianren'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='tuijianren',
            field=models.CharField(default='', max_length=100, verbose_name='推荐人'),
        ),
    ]
