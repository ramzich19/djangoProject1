from modeltranslation.translator import register,TranslationOptions
from .models import Articles


@register(Articles)
class ArticlesTranslationOptions(TranslationOptions):
    fields = ('name','text',)


# @register(Comments)
# class CommentsTranslationOptions(TranslationOptions):
#     fields = ('text',)
