from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField

from django_translations.apps.translation.models import Translation, PostTranslation, Post


class TranslationSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Translation, read_only=False)

    class Meta:
        model = Translation
        fields = ('id', 'title', 'translations')


class PostTranslationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTranslation
        fields = ('id', 'title', 'body', 'master')


class PostSerializer(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Post)
    # translations = PostTranslationSerializer(many=True,)
    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'body', 'translations', 'language_code',)

# class PostSerializer(serializers.ModelSerializer):
#     # translations = TranslatedFieldsField(shared_model=Post)
#     # translations = PostTranslationSerializer(many=True,)
#     class Meta:
#         model = Post
#         fields = ('id', 'slug', 'title', 'body', 'translations')
