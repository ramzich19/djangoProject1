from django.contrib import admin
from core.models import Articles,Comments,Category
from modeltranslation.admin import TranslationAdmin
# Register your models here.

admin.site.register(Articles)
admin.site.register(Comments)
admin.site.register(Category)


# @admin.register(Articles)
# class ArticlesAdmin(TranslationAdmin):
#     list_display = ('name','text')
