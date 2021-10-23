from rest_framework import serializers

from ..models import WordTranslation


class WordTranslationM2MSerializer(serializers.ModelSerializer):
    class Meta:
        model = WordTranslation
        fields = [
            'id',
            'word',
            'language',
        ]


class WordTranslationSerializer(serializers.ModelSerializer):
    translations = WordTranslationM2MSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = WordTranslation
        fields = [
            'id',
            'word',
            'language',
            'description',
            'translations',
        ]
