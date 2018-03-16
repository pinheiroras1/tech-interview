from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import Articles
from . models import Item
from . models import Carts
from . serializers import ArticleSerializer
from . serializers import CartsSerializer
from . serializers import ItemSerializer


class articleList(APIView):
    def get(self, request):
        article = Articles.objects.all()
        serializer = ArticleSerializer(article, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def post(self, request):
        serializer = ArticleSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
