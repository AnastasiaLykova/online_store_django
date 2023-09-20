from django import forms

from blog.models import Article
from catalog.models import Product


class StyleFormMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ArticleForm(StyleFormMixin, forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body', 'preview',)
