from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

from django_translations.apps.translation.models import Translation


class TranslationSerializer(TranslatableModelSerializer):
    # translations = TranslatedFieldsField(shared_model=Translation, read_only=False)

    class Meta:
        model = Translation
        fields = ('id', 'title', 'translations')
