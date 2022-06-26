from django.db import models

"""Абстрактная модель, которая записывает дату создания и обновления записи в бд"""
class CreateUpdateMixin(models.Model):
    created = models.DateTimeField('Дата создания', auto_now_add=True)
    updated = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        abstract = True
