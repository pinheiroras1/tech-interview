from rest_framework import serializers

from .models import Articles
from .models import Carts
from .models import Item


class ArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Articles
        fields = '__all__'


class CartsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carts
        fields = '__all__'


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = '__all__'
