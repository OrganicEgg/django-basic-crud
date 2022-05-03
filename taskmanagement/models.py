from pyexpat import model
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Task(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    status = models.IntegerField()
    assigned_to_user_id = models.IntegerField()
    created_by_user_id = models.IntegerField()
    last_updated_by_user_id = models.IntegerField(default=None, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated_date = models.DateTimeField(default=None, blank=True, null=True)

    def __str__(self):
        return "[" + str(self.id) + "] " + self.name
