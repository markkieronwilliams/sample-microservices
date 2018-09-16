from django.db import models
import uuid

class Attempt(models.Model):
    id = models.UUIDField(primary_key=True,
                          unique=True,
                          default=uuid.uuid4)
    user_id = models.UUIDField()
    score = models.IntegerField()
