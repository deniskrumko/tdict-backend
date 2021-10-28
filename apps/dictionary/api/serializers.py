from rest_framework import serializers

from ..models import WordTranslation


class WordTranslationSerializer(serializers.ModelSerializer):
    """Serializer for ``WordTranslation`` model."""

    class Meta:
        model = WordTranslation
        fields = [
            'id',
            'word_from',
            'word_to',
            'language_from',
            'language_to',
            'description',
        ]
