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


class PostTranslation(TranslatedFieldsModel):
    master = models.ForeignKey(Post, related_name='translations', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    body = models.TextField()

