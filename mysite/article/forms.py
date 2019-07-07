from django import forms
from article.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title': "Custom_title",
            'description': "Custom_description"
        }
