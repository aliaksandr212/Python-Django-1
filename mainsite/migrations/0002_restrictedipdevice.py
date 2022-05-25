# Generated by Django 2.0 on 2018-10-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RestrictedIPDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, help_text='user ID', max_length=50, null=True)),
                ('ip_device', models.CharField(blank=True, help_text='Restricted IP address or device', max_length=250, null=True)),
                ('blocked_by_admin', models.BooleanField(default=False, help_text='This field show IP or Device is blocked by admin', verbose_name='active')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]