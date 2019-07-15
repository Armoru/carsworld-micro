from django.conf.urls import url
from django.urls import include
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view

from .views import CategoryViewSet, NewsViewSet

schema_view = get_swagger_view(title='Blog API')

router = routers.DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('news', NewsViewSet)

urlpatterns = [
    url('docs/', schema_view)
]

urlpatterns += router.urls
