from django.db import models

from .resources import LANGUAGE_CHOICES, Language


class WordTranslation(models.Model):
    """Model for single word translation."""

    # Main fields
    word_from = models.CharField(
        max_length=512,
        null=True,
        blank=False,
        verbose_name='Word (From)',
    )
    word_to = models.CharField(
        max_length=512,
        null=True,
        blank=False,
        verbose_name='Word (To)',
    )
    language_from = models.CharField(
        max_length=2,
        null=True,
        blank=False,
        choices=LANGUAGE_CHOICES,
        default=Language.EN.name,
        verbose_name='Language (From)',
    )
    language_to = models.CharField(
        max_length=2,
        null=True,
        blank=False,
        choices=LANGUAGE_CHOICES,
        default=Language.RU.name,
        verbose_name='Language (To)',
    )
    description = models.TextField(
        null=True,
        blank=True,
        verbose_name='Description',
    )

    # Extra info fields
    author = models.ForeignKey(
        'users.User',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='words',
        verbose_name='Author',
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created',
    )
    modified = models.DateTimeField(
        auto_now=True,
        verbose_name='Modified',
    )

    def __str__(self):
        return f'{self.word_from} - {self.word_to}'

    class Meta:
        verbose_name = 'Word translation'
        verbose_name_plural = 'Word translations'
        unique_together = ('word_from', 'word_to')
        ordering = ('-modified',)
