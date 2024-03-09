from django.db import models
from .county_models import *

class GroupType1County3(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(CountyType1, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type1County3グループ'
        verbose_name_plural = 'Type1County3グループ'
        db_table = 'type1county3group'


class GroupType2County3(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(CountyType2, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type2County3グループ'
        verbose_name_plural = 'Type2County3グループ'
        db_table = 'type2county3group'



class GroupType3County1(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(CountyType3, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Type3County1グループ'
        verbose_name_plural = 'Type3County1グループ'
        db_table = 'type3county1group'