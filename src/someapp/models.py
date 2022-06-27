from django.db import models
from core.models import CreateUpdateMixin


class Album(CreateUpdateMixin):
    id = models.AutoField(primary_key=True, null=False)
    name = models.CharField('Название альбома', max_length=100)
    artist = models.CharField('Артист', max_length=100)
    poster = models.ImageField('Обложка альбома')

    class Meta:
        db_table = 'album'
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'
        unique_together = ['name', 'artist']

    def __str__(self) -> str:
        return f'{self.artist}: {self.name}'


class Track(CreateUpdateMixin):
    id = models.AutoField(primary_key=True, null=False)
    album = models.ForeignKey(
        Album, related_name='tracks', on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField('Номер композиции')
    title = models.CharField('Название композиции', max_length=100)
    duration = models.PositiveSmallIntegerField('Длительность в секундах')

    class Meta:
        db_table = 'track'
        verbose_name = 'Композиция'
        verbose_name_plural = 'Композиции'
        unique_together = ['album', 'order']

    def __str__(self) -> str:
        return f'{self.order}: {self.title}'
