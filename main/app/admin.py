from django.contrib import admin
from .models import cards_s,Category,card_detail
# Register your models here.
admin.site.register(cards_s)

admin.site.register(Category)
admin.site.register(card_detail)