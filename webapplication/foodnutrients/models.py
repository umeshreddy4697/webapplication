from django.db import models

class nutrients(models.Model):
    nid=models.CharField(max_length=20)
    nname=models.CharField(max_length=100)
    class Meta:
        db_table="nutrients"







