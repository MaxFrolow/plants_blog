from django.db import models
from django.contrib.postgres.fields import ArrayField

from django.utils.translation import ugettext_lazy as _



class PlantPost(models.Model):
    title = models.CharField(_('Заголовок'),max_length=100, blank=False)
    image = models.ImageField(_('Титульне зображення'))
    text = models.TextField(_('Текст статті'), blank=False)
    created = models.DateTimeField(_('Дата написання'), auto_now_add=True)
    updated = models.DateTimeField(_('Дата останнього редагування'), auto_now_add=True)
    tags = ArrayField( models.CharField(_('Теги'), max_length=25), blank=False)
    show = models.BooleanField(_('Готово для показу'), default=False)
    is_favorite = models.BooleanField(_('Улюблене'), default=False)

    class Meta:
        ordering = ('-created',)
        verbose_name = ('Стаття')
        verbose_name_plural = ('Статті')


#class ConnectedPost(models.Model):