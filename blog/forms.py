from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'image','description', 'content']  
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
            'summary': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
            'content': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        }
