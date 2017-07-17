from django.db import models
from datetime import datetime

class projectscopy(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=500, null=True)
    projectmanager = models.CharField(max_length=100, null=True)
    createdon = models.DateTimeField(default=datetime.now)
    updatedon = models.DateTimeField(default=datetime.now)

    class Meta:
        db_table = 'projectscopy'

