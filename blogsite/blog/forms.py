from django import forms
from .models import PostModel, Comment,PostSection
from django.forms import formset_factory



class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':7}))
    class Meta:
        model = PostModel
        fields = ('title', 'content','image')

class PostSectionForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':7}))
    class Meta:
        model = PostSection
        fields = ( 'content','image')
        

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','content','image')

class PostApproveForm(forms.ModelForm):
     class Meta:
        model = PostModel
        fields = ('is_approved',)

class CommentForm(forms.ModelForm):
    content = forms.CharField(label='',widget=forms.TextInput(attrs={'placeholder': 'Add comment here...'}))
    class Meta:
        model = Comment
        fields = ('content',)