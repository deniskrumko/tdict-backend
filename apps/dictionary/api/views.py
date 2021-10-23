from rest_framework import authentication, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import WordTranslation
from .serializers import WordTranslationSerializer


class WordTranslationViewSet(viewsets.ModelViewSet):
    # authentication_classes = (
    #     authentication.TokenAuthentication,
    # )
    # permission_classes = (
    #     IsAuthenticated,
    # )
    queryset = WordTranslation.objects.all()
    serializer_class = WordTranslationSerializer

    # def filter_queryset(self, queryset):
    #     """Filter queryset for current user only."""
    #     return queryset.filter(author=self.request.user)

    # def perform_create(self, serializer):
    #     """Set author to saved word translation."""
    #     serializer.save(author=self.request.user)
