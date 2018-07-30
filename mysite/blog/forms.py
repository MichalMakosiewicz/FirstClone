from django import forms
from blog.models import Post,Comment

class PostForm(form.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editble medium-editor-textarea postcontent'}),
        }

class CommentForm(form.ModleForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editble medium-editor-textarea'}),
        }
