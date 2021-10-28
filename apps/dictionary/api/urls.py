from rest_framework.routers import DefaultRouter

from .views import WordTranslationViewSet

router = DefaultRouter()

router.register(r'words', WordTranslationViewSet)
