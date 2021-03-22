from rest_framework import viewsets

from .serializers import TranslationSerializer
from django_translations.apps.translation.models import Translation


class TranslationViewSet(viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()
    # queryset = Translation.objects.prefetch_related('translations').all()

    def get_queryset(self):
        queryset = super().get_queryset()
        if 'language' in self.request.query_params:
            queryset = queryset.language(self.request.query_params.get('language', None))
        return queryset
