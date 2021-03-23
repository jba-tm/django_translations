from django.contrib import admin

from parler.admin import TranslatableAdmin, TranslatableModelForm, TranslatableTabularInline

from .models import Translation, PostTranslation, Post


class TranslationAdmin(TranslatableAdmin):
    form = TranslatableModelForm

    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'title': ('title',)
        }


# class PostTranslationTabularInline(TranslatableTabularInline):
#     model = PostTranslation


class PostAdmin(TranslationAdmin):
    form = TranslatableModelForm

    # inlines = [PostTranslationTabularInline]

    def get_prepopulated_fields(self, request, obj=None):
        # can't use `prepopulated_fields = ..` because it breaks the admin validation
        # for translated fields. This is the official django-parler workaround.
        return {
            'title': ('title',),
            'body': ('body',)
        }


class PostTranslationAdmin(admin.ModelAdmin):
    list_display = ('title', 'master')
    # pass


admin.site.register(Post, PostAdmin)
admin.site.register(PostTranslation, PostTranslationAdmin)
admin.site.register(Translation, TranslationAdmin)
