from django.db import models

class menu_item(models.Model):
    name = models.CharField(max_length=50)
    ref = models.CharField(max_length=500)
