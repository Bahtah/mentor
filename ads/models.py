from django.db import models
from django.utils import timezone

from users.models import User


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class SubCategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="название")
    category = models.ForeignKey(Category,on_delete=models.CASCADE, verbose_name="категория")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="дата")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Подкатегрия"
        verbose_name_plural = "Подкатегории"


class Ads(models.Model):
    LEARN = "Хочу научиться"
    TEACH = "Могу научить"
    TYPE_OF_ADS = [
        (LEARN,"Хочу научиться"),
        (TEACH,"Могу научить"),
    ]

    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True, related_name='ads')
    title = models.CharField(max_length=150, verbose_name="название")
    description = models.TextField(verbose_name="описание")
    price = models.FloatField(verbose_name="цена")
    image = models.ImageField(upload_to="images/ads/", verbose_name="фото")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ads', null=True, blank=True)
    type = models.CharField(max_length=100,choices=TYPE_OF_ADS, default=LEARN, verbose_name="тип")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="создано")
    update_at = models.DateTimeField(auto_now=True, verbose_name="обновлено")
    
    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Обьявление"
        verbose_name_plural = "Обьявления"