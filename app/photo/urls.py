
from photo.views import PhotoViewSet
from rest_framework.routers import DefaultRouter

api = DefaultRouter()
api.register('', PhotoViewSet)

urlpatterns = api.urls