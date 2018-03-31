from django.db import models
from django.conf import settings


class Blog(models.Model):
    ''' Blog model '''

    # Fk fields
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs', blank=True, null=True)
    category = models.ForeignKey('blog.Category', related_name='blogs', blank=True, null=True)


    title = models.CharField('Titulo', max_length=255, default='')
    description = models.CharField('Descripción', max_length=255, blank=True, default='')
    content = models.TextField('Contenido', blank=True, default='')

    # Util datatimes
    created_at = models.DateTimeField("Fecha de creación", auto_now_add=True)
    last_modified = models.DateTimeField("Última modificación", auto_now=True)

    def __str__(self):
        ''' Define str of model '''
        return self.title



class Category(models.Model):
    ''' Category Model '''
    name = models.CharField('Nombre', max_length=255, blank=True, default='')
    description = models.CharField('Descripción', max_length=255, blank=True, default='')

    def __str__(self):
        ''' Define str of model '''
        return self.name
