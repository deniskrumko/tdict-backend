from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from ..models import WordTranslation


class BaseWordTranslationSerializer(serializers.ModelSerializer):
    """Base serializer for ``WordTranslation`` model."""

    class Meta:
        model = WordTranslation
        fields = [
            'id',
            'word',
            'language',
            'description',
            'translations',
        ]

    def validate(self, data):
        """Validate data on update/create."""
        if 'translations' in data:
            user = self.context['request'].user
            for word in data['translations']:
                if self.instance == word:
                    raise ValidationError({
                        'translations': ['You cannot add word as self translation'],
                    })

                if word.author != user:
                    raise ValidationError({
                        'translations': [f'Word ({word.id}) does not belong to current user'],
                    })

        return super().validate(data)


class TranslationsSerializer(BaseWordTranslationSerializer):
    """Serializer for nested translations."""

    class Meta(BaseWordTranslationSerializer.Meta):
        fields = [
            'id',
            'word',
            'language',
        ]


class NestedWordTranslationSerializer(BaseWordTranslationSerializer):
    """Serializer for word translation with nested translations."""

    translations = TranslationsSerializer(many=True, read_only=True)


class WordTranslationSerializer(BaseWordTranslationSerializer):
    """Default word translation serializer."""
