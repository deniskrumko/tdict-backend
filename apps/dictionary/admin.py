from django.contrib import admin

from . import models


class WordTranslationInline(admin.TabularInline):
    """Inline class for ``WordTranslation`` model."""

    model = models.WordTranslationRelation
    fk_name = 'source'
    extra = 0
    autocomplete_fields = ('destination',)


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
            ),
        }),
        ('Dates', {
            'fields': (
                'created',
                'modified',
            ),
        }),
    )
    list_display = (
        'word',
        'language',
        'description',
        'author',
        'created',
        'modified',
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
    inlines = (
        WordTranslationInline,
    )

    def save_model(self, request, obj, form, change):
        """Save model and set author."""
        if obj and not obj.author:
            obj.author = request.user

        return super().save_model(request, obj, form, change)
