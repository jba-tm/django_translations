from rest_framework import routers

from .views import TranslationViewSet, PostViewSet, PostTranslationViewSet


router = routers.DefaultRouter()

router.register('translation', TranslationViewSet)
router.register('post', PostViewSet)
router.register('post-translation', PostTranslationViewSet)
