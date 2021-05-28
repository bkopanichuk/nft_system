from . import serializers
from . import models
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions
from rest_framework.response import Response

class BaseTokenViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `LIST`, `CREATE`, `RETRIEVE`,
    `UPDATE` and `DESTROY` actions.
    """

    serializer_class = serializers.BaseTokenSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = models.BaseToken.objects.all()
    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        return models.BaseToken.objects.filter(user=user)

class MetadataViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `LIST`, `CREATE`, `RETRIEVE`,
    `UPDATE` and `DESTROY` actions.
    """

    serializer_class = serializers.MetadataSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = models.Metadata.objects.all()