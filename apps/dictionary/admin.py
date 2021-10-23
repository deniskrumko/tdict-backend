from django.contrib import admin
from django.contrib import messages
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
    actions = (
        'change_author',
    )

    def save_model(self, request, obj, form, change):
        """Save model and set author."""
        if obj and not obj.author:
            obj.author = request.user

        return super().save_model(request, obj, form, change)

    def _translations(self, obj):
        """Get translations."""
        return ','.join(obj.translations.values_list('word', flat=True))

    def change_author(self, request, queryset):
        """Change words author to current user."""
        count = queryset.update(author=request.user)
        return messages.add_message(
            request,
            messages.SUCCESS,
            f'{count} words were successfully updated',
        )

    change_author.label = 'Change word author to CURRENT user'
    change_author.short_description = 'Change word author to CURRENT user'

    _translations.short_description = 'Translations'
