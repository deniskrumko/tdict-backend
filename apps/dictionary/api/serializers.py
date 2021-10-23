from rest_framework import serializers

from ..models import WordTranslation


class WordTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordTranslation
        fields = [
            'id',
            'word',
            'language',
            'description',
            'created',
            'modified',
            'translations',
        ]
