from django.db import models
from .type_models import *

class CountyType1(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(TypeCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Type1群'
        verbose_name_plural = 'Type1群'
        db_table = 'type1county'


class CountyType2(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(TypeCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Type2群'
        verbose_name_plural = 'Type2群'
        db_table = 'type2county'


class CountyType3(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    category = models.ForeignKey(TypeCategory, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Type3群'
        verbose_name_plural = 'Type3群'
        db_table = 'type3county'
