from django.contrib.auth.models import User
from rest_framework import serializers
from .models import projectscopy

class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = projectscopy
        fields = ('id', 'name', 'description', 'projectmanager', 'createdon', 'updatedon')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')
