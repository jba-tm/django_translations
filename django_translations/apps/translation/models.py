from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Translation(TranslatableModel):
    translations = TranslatedFields(
        title=models.CharField(max_length=200, unique=True,)
    )

    def __unicode__(self):
        return self.title
