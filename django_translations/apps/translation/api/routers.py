from rest_framework import routers

from .views import TranslationViewSet


router = routers.DefaultRouter()

router.register('translation', TranslationViewSet)
