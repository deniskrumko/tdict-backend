from django.contrib import admin, messages

from . import models


@admin.register(models.WordTranslation)
class WordTranslationAdmin(admin.ModelAdmin):
    """Admin class for ``WordTranslation`` model."""

    fieldsets = (
        ('From', {
            'fields': (
                'word_from',
                'language_from',
                'description',
            ),
        }),
        ('To', {
            'fields': (
                'word_to',
                'language_to',
            ),
        }),
        ('Other', {
            'fields': (
                'source',
                'author',
                'created',
                'modified',
            ),
        }),
    )
    list_per_page = 50
    list_display_links = (
        'id',
        'word_from',
    )
    list_display = (
        'id',
        'word_from',
        'word_to',
        'language_from',
        'language_to',
        'description',
        'author',
    )
    list_filter = (
        'language_from',
        'language_to',
    )
    search_fields = (
        'word_from',
        'word_to',
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
