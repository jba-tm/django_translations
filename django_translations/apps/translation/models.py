from django.db import models
from parler.models import TranslatableModel, TranslatedFields, TranslatedField, TranslatedFieldsModel


class Translation(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, unique=True, )
    )


class Post(TranslatableModel):
    slug = models.SlugField(unique=True, max_length=250)
    title = TranslatedField()
    body = TranslatedField()

    # translations = TranslatedFields(
    #     title=models.CharField(max_length=200, unique=True, ),
    #     body = models.TextField(max_length=5000)
    # )

    def __str__(self):
        return self.slug

    # def get_fallback_languages(self):
    #     return []

    def get_translation(self, language_code, related_name=None):
        """
        Fetch the translated model
        """
        print('get')
        meta = self._parler_meta._get_extension_by_related_name(related_name)
        return self._get_translated_model(language_code, meta=meta, auto_create=True)

    def safe_translation_getter(self, *args, **kwargs):
        return super().safe_translation_getter(*args, **kwargs)


class PostTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(Post, related_name='translations', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()

