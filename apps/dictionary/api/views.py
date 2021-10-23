from rest_framework import authentication, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import WordTranslation
from .serializers import WordTranslationSerializer


class WordTranslationPublicViewSet(viewsets.ModelViewSet):
    """Public view for development only."""

    queryset = WordTranslation.objects.filter(language='EN')  # TODO: remove this
    serializer_class = WordTranslationSerializer


class WordTranslationPrivateViewSet(WordTranslationPublicViewSet):
    """View to make CRUD operations with word translations."""

    authentication_classes = (
        authentication.TokenAuthentication,
    )
    permission_classes = (
        IsAuthenticated,
    )

    def filter_queryset(self, queryset):
        """Filter queryset for current user only."""
        return queryset.filter(author=self.request.user)

    def perform_create(self, serializer):
        """Set author to saved word translation."""
        serializer.save(author=self.request.user)
