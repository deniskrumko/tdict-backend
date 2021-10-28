from django.db import models

from rest_framework import authentication, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import WordTranslation
from .serializers import WordTranslationSerializer


class WordTranslationViewSet(viewsets.ModelViewSet):
    """View to make CRUD operations with word translations."""

    queryset = WordTranslation.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = WordTranslationSerializer

    def filter_queryset(self, queryset):
        """Filter queryset."""
        language_from = self.request.query_params.get('language_from')
        if language_from:
            queryset = queryset.filter(language_from=language_from)

        language_to = self.request.query_params.get('language_to')
        if language_to:
            queryset = queryset.filter(language_to=language_to)

        search_query = self.request.query_params.get('q')
        if search_query:
            queryset = queryset.filter(
                models.Q(word_from__icontains=search_query)
                | models.Q(word_to__icontains=search_query)
                | models.Q(description__icontains=search_query),
            )

        return queryset.filter(author=self.request.user)

    def perform_create(self, serializer):
        """Set author to saved word translation."""
        serializer.save(author=self.request.user)
