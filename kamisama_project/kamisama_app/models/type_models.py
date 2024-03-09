from django.db import models

class TypeCategory(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=200)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = '類型'
        verbose_name_plural = '類型'
        db_table = 'type'


