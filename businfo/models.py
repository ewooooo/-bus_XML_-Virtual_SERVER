from django.db import models

# Create your models here.

class bus(models.Model):
    routeId = models.CharField(max_length=10, primary_key=True)
    버스번호 = models.CharField(max_length=5, default='4')
    현재위치 = models.CharField(max_length=5, default='3')
    번호판 = models.CharField(max_length=15, default='경기70바5703')


    class Meta:
        ordering = ['버스번호']
