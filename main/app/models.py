from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150)
    def __str__(self) :
        return self.name
# Create your models here.
class cards_s(models.Model):
    name = models.CharField(max_length=350)
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=False, null=True)
    def __str__(self) :
        return self.name
class card_detail(models.Model):
    name =models.CharField(max_length=150)
    foto = models.URLField(blank=True,null=True)
    foto1 = models.URLField(blank=True,null=True)

    card=models.ForeignKey(cards_s,on_delete=models.CASCADE)