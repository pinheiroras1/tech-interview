from django.contrib import admin
from .models import Articles
from .models import Item
from .models import Carts

admin.site.register(Articles)
admin.site.register(Item)
admin.site.register(Carts)
