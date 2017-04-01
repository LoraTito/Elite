from django.db import models


class HorseForSale(models.Model):
    name = models.CharField(max_length=128, verbose_name='Име')
    gender = models.CharField(max_length=128)
    breed = models.CharField(max_length=128, blank=True)
    height = models.CharField(max_length=128, blank=True)
    date_of_birth = models.CharField(max_length=128, blank=True)
    price = models.CharField(max_length=128)
    main_image = models.ImageField()
    date_of_listing = models.DateField(auto_now_add=True)
    video_embed_code = models.TextField(blank=True)

    class Meta:
        ordering = ['date_of_listing', 'name']
        verbose_name = 'Кон за продажба'
        verbose_name_plural = 'Коне за продажба'


class ImageGallery(models.Model):
    image = models.ImageField()

    class Meta:
        verbose_name = 'Снимка'
        verbose_name_plural = 'Снимки'
