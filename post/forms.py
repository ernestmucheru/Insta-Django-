from django import forms
from post.models import Post

class NewPostForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

    class Meta:
        model = Post
        fields = ('image','caption','tags')