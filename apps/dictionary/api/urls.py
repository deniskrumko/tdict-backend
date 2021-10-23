from rest_framework.routers import DefaultRouter

from .views import WordTranslationPrivateViewSet, WordTranslationPublicViewSet

router = DefaultRouter()

# TODO: Remove public API
router.register(r'public/words', WordTranslationPublicViewSet)

router.register(r'words', WordTranslationPrivateViewSet)
