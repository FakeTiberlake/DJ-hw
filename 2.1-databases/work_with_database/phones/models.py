from django.db import models
from django.urls import reverse
# from autoslug import AutoSlugField


class Phone(models.Model):
    name = models.CharField(max_length=250, db_index=True, verbose_name='Название')
    price = models.CharField(max_length=10, db_index=True, verbose_name='Цена')
    image = models.ImageField(db_index=True, verbose_name='Изображение')
    release_date = models.DateField(max_length=50, db_index=True, verbose_name='Дата выхода')
    lte_exists = models.BooleanField(verbose_name='Поддержка LTE')
    slug = models.SlugField(max_length=250, unique=True, db_index=True, verbose_name='URL')

    def get_absolute_url(self):
        return reverse('phone', kwargs={'slug': self.slug})





