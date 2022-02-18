from django.db import models

# Create your models here.
from core.models import BaseModel


class ContactUs(BaseModel):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    text = models.TextField()
