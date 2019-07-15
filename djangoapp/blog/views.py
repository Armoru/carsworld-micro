from rest_framework import permissions, viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.response import Response

# Create your views here.
from .models import Category, News
from .serializers import CategorySerializer, NewsSerializer


# 01 Hello World
@api_view(["GET"])
def hello_world(request):
    return Response({"message": "hello world"})

# 02 Simplest GET all data
@api_view(["GET"])
def categories(request):
    queryset = Category.objects.all()
    serialized = CategorySerializer(queryset, many=True)
    return Response(serialized.data)

# 03 Simplest GET all data
@api_view(["GET"])
def single_category(request, pk):
    queryset = Category.objects.get(pk=pk)
    serialized = CategorySerializer(queryset)
    return Response(serialized.data)


# Skip generic view, kita langsung ke ModelViewSet
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
