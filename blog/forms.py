from django.forms import ModelForm, fields
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = '__all__' # ['title_review', 'comment', 'notation']