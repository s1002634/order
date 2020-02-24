from django.db import models

# Create your models here.
class Url(models.Model):
    # 短url
    short_url=models.CharField(max_length=255)
    # 原始url
    ori_url = models.TextField()
    
    