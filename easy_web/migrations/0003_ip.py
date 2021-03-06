# Generated by Django 3.1 on 2020-09-06 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easy_web', '0002_component'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('ip_address', models.GenericIPAddressField(primary_key=True, serialize=False)),
                ('visit_count', models.IntegerField(default=0)),
                ('country', models.CharField(default='None', max_length=100)),
                ('city', models.CharField(default='None', max_length=100)),
                ('lat', models.DecimalField(decimal_places=4, default='0', max_digits=6)),
                ('lon', models.DecimalField(decimal_places=4, default='0', max_digits=6)),
            ],
        ),
    ]
