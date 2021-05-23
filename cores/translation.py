from modeltranslation.translator import register,TranslationOptions
from .models import Articles


@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ('name','text','text1','text2')
