from enum import Enum


class Language(Enum):
    EN = 'EN'
    RU = 'RU'


LANGUAGE_CHOICES = (
    (Language.EN.name, '🇬🇧 English'),
    (Language.RU.name, '🇷🇺 Russian'),
)
