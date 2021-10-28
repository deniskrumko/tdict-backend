from rest_framework import authentication, viewsets
from rest_framework.permissions import IsAuthenticated

from ..models import WordTranslation
from .serializers import NestedWordTranslationSerializer, WordTranslationSerializer


class WordTranslationViewSet(viewsets.ModelViewSet):
    """View to make CRUD operations with word translations."""

    queryset = WordTranslation.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_classes = {
        'list': NestedWordTranslationSerializer,
        'retrieve': NestedWordTranslationSerializer,
        '__default__': WordTranslationSerializer,
    }

    def filter_queryset(self, queryset):
        """Filter queryset."""
        language = self.request.query_params.get('language')
        if language:
            queryset = queryset.filter(language=language)

        return queryset.filter(author=self.request.user)

    def perform_create(self, serializer):
        """Set author to saved word translation."""
        serializer.save(author=self.request.user)

    def get_serializer_class(self):
        """Get serializer class depending on action type."""
        classes_map = self.serializer_classes
        return classes_map.get(self.action, classes_map['__default__'])
