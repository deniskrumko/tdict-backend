from rest_framework import authentication, viewsets

from ..models import WordTranslation
from .serializers import WordTranslationSerializer


class WordTranslationViewSet(viewsets.ModelViewSet):
    # authentication_classes = (authentication.SessionAuthentication, authentication.BasicAuthentication)
    queryset = WordTranslation.objects.all()
    serializer_class = WordTranslationSerializer
