from rest_framework import routers

from django_translations.apps.translation.api.views import PostTranslationViewSet, TranslationViewSet, PostViewSet

router = routers.DefaultRouter()

router.register('post', PostViewSet)
router.register('post-translation', PostTranslationViewSet)
router.register('translation', TranslationViewSet)
