from photo.models import Thing, Country, City, Photo
from rest_framework.serializers import ModelSerializer


class ThingSerializer(ModelSerializer):
    class Meta:
        model = Thing
        fields = ('name',)


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = ('name',)


class CitySerializer(ModelSerializer):
    country = CountrySerializer()

    class Meta:
        model = City
        fields = ('name', 'country')


class PhotoSerializer(ModelSerializer):
    things = ThingSerializer(many=True, required=False)
    city = CitySerializer(required=False)

    class Meta:
        model = Photo
        fields = ('id', 'title', 'author', 'accepted_by',
                  'city', 'things', 'image', 'is_accepted')
        extra_kwargs = {
            'author': {'read_only': True},
            'accepted_by': {'read_only': True}
        }
