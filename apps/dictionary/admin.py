from django.contrib import admin

from . import models


@admin.register(models.WordTranslation)
class WordTranslationAdmin(admin.ModelAdmin):
    """Admin class for ``WordTranslation`` model."""

    fieldsets = (
        (None, {
            'fields': (
                'word',
                'language',
                'description',
                'author',
                'translations',
            ),
        }),
        ('Dates', {
            'fields': (
                'created',
                'modified',
            ),
        }),
    )
    autocomplete_fields = (
        'translations',
    )
    list_per_page = 20
    list_display_links = (
        'id',
        'word',
    )
    list_display = (
        'id',
        'word',
        'language',
        'description',
        'author',
        '_translations',
    )
    list_filter = (
        'language',
    )
    search_fields = (
        'word',
        'description',
    )
    readonly_fields = (
        'author',
        'created',
        'modified',
    )

    def save_model(self, request, obj, form, change):
        """Save model and set author."""
        if obj and not obj.author:
            obj.author = request.user

        return super().save_model(request, obj, form, change)

    def _translations(self, obj):
        x = obj.translations.values_list('word', flat=True)
        return ','.join(x)

    _translations.short_description = 'Translations'
