from django.conf import settings
from django.core.management import BaseCommand

from apps.users.models import User

from ...models import WordTranslation
from ...resources import Language

description_templates = {
    Language.RU: 'Описание для {}',
    Language.EN: 'Description for {}',
}


class Command(BaseCommand):
    """Command to populate database with test data."""

    def handle(self, *args, **options):
        """Execute command."""
        with open(f'{settings.BASE_DIR}/apps/dictionary/management/commands/words.txt', 'r') as f:
            lines = f.readlines()

        superuser = User.objects.filter(is_superuser=True).first()
        if not superuser:
            self.stdout.write(self.style.ERROR('Create superuser before running this command'))

        for line in lines:
            ru_word, en_word, _ = line.split('\t')

            WordTranslation.objects.update_or_create(
                word_from=en_word.split(',')[0],
                word_to=ru_word.split(',')[0],
                language_from=Language.EN.value,
                language_to=Language.RU.value,
                description=None,
                author=superuser,
            )

        self.stdout.write(self.style.SUCCESS('Word translations are successfully created'))
