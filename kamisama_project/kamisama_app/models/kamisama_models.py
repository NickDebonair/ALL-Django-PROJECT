from django.db import models
from ..models import *
from .type_models import *
from .county_models import *
from .group_models import *
from .test2_models import *

class Kamisama(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(TaggedItem,
                    on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '神'
        verbose_name_plural = '神々'
        db_table = 'kamisama'

class God(models.Model):
    name = models.CharField(max_length=20)