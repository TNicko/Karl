# Generated by Django 4.1.5 on 2023-01-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_url', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('task_id', models.CharField(blank=True, max_length=150, null=True)),
                ('task_status', models.CharField(blank=True, choices=[('started', 'started'), ('running', 'running'), ('finished', 'finished'), ('failed', 'failed'), ('ready', 'ready'), ('pending', 'pending')], default='ready', max_length=15, null=True)),
                ('content', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('last_modified', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='ScrapedWebsite',
        ),
    ]
