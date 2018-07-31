from django.contrib.auth.models import User
from .models import Missionary, Update
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class MissionarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Missionary
        fields = ('friendly_name', 'email')


class UpdateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Update
        fields = ('missionary', 'date_of_update', 'date_publish_start', 'date_publish_end', 'content')