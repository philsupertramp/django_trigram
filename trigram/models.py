from django.contrib.postgres.search import TrigramSimilarity
from django.db import models

# Create your models here.
from django.db.models.functions import Greatest


class ModelA(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class ModelB(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return ' '.join([self.first_name, self.last_name])


class ModelCManager(models.Manager):
    def search(self, value):
        qs = self.annotate(
            sim=Greatest(
                TrigramSimilarity('a__title', value),
                TrigramSimilarity('b__first_name', value)
                + TrigramSimilarity('b__last_name', value)
            )
        ).filter(sim__gt=0)
        return qs


class ModelC(models.Model):
    a = models.ForeignKey(ModelA, on_delete=models.PROTECT)
    b = models.ForeignKey(ModelB, on_delete=models.PROTECT)

    objects = ModelCManager()

    def __str__(self):
        return '{} <–> {}'.format(self.b, self.a)
