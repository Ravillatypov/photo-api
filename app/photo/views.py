from photo.serializers import PhotoSerializer
from photo.models import Photo
from rest_framework.viewsets import ModelViewSet


class PhotoViewSet(ModelViewSet):
    queryset = Photo.objects.get_accepted()
    def get_queryset(self):
        if hasattr(self, 'request') and hasattr(self.request, 'user'):
            return Photo.objects.get_queryset_by_user(self.request.user)
        return Photo.objects.get_accepted()

    serializer_class = PhotoSerializer
