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
            words = {
                Language.RU: ru_word,
                Language.EN: en_word,
            }

            instances = []
            for language, word in words.items():
                word = word.split(',')[0]
                word_instance, _ = WordTranslation.objects.update_or_create(
                    word=word,
                    language=language.value,
                    description=description_templates[language].format(word),
                    author=superuser,
                )
                instances.append(word_instance)

            instances[0].translations.add(instances[1])

        self.stdout.write(self.style.SUCCESS('Word translations are successfully created'))
