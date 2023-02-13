from django.db import models

# Create your models here.

class Session(models.Model):
    TASK_STATUSES = (
        ('started', 'started'),
        ('running', 'running'),
        ('finished', 'finished'),
        ('failed', 'failed'),
        ('ready', 'ready'),
        ('pending', 'pending'),
    )
    search_url = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    task_id = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=15, default='ready', choices=TASK_STATUSES, blank=True, null=True)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

class WebsitePage(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    url = models.CharField(max_length=300, unique=True, blank=False, null=False)
    content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

