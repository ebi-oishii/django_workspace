import uuid
from django.db import models

from accounts.models import User

class Category(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=32, null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    is_payment = models.BooleanField(default=True)
