from tabnanny import verbose
from django.db import models

class Others(models.Model):
    name = models.CharField(max_length=20, default='その他')

    def __str__(self):
        return 'その他'

    class Meta:
        verbose_name = 'その他'
        verbose_name_plural = 'その他'