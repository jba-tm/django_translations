from django.contrib import admin

from parler.admin import TranslatableAdmin, TranslatableModelForm

from .models import Translation


class TranslationAdmin(TranslatableAdmin):
    form = TranslatableModelForm

    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'title': ('title',)
        }


admin.site.register(Translation, TranslationAdmin)
