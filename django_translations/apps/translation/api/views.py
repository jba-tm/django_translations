import json

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers import TranslationSerializer, PostTranslationSerializer, PostSerializer
from django_translations.apps.translation.models import Translation, Post, PostTranslation


class LanguageParam:
    def get_queryset(self):
        queryset = super().get_queryset()
        if 'language' in self.request.query_params:
            queryset = queryset.language(self.request.query_params.get('language', None))
            # queryset.
        return queryset


class TranslationViewSet(LanguageParam, viewsets.ModelViewSet):
    serializer_class = TranslationSerializer
    queryset = Translation.objects.all()
    # queryset = Translation.objects.prefetch_related('translations').all()


class PostViewSet(LanguageParam, viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.prefetch_related('translations').all()

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        # instance.translations.exclude(language_code__in=request.data['translations'].keys()).delete()
        instance.translations.exclude(language_code__in=request.data['translations'].keys()).delete()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)


class PostTranslationViewSet(viewsets.ModelViewSet):
    serializer_class = PostTranslationSerializer
    queryset = PostTranslation.objects.all()
