# Generated by Django 2.0.2 on 2018-08-04 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20180804_1419'),
    ]

    operations = [
        migrations.RenameField(
            model_name='danwei',
            old_name='dianhua2',
            new_name='lian_xi_dian_hua',
        ),
        migrations.RenameField(
            model_name='danwei',
            old_name='dianhua1',
            new_name='lian_xi_ren',
        ),
        migrations.AddField(
            model_name='danwei',
            name='lian_xi_di_zhi',
            field=models.CharField(default='', max_length=200, verbose_name='联系地址'),
            preserve_default=False,
        ),
    ]