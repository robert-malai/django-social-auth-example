from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from .models import projectscopy
from .serializer import ProjectsSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class ProjectsViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = projectscopy.objects.all()
    serializer_class = ProjectsSerializer

    def list(self, request):
        queryset = projectscopy.objects.all()
        serializer = ProjectsSerializer(queryset, many=True)
        return Response(serializer.data)

class UserViewSet(viewsets.ViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def list(self, request):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        return Response(serializer.data)
