from crispy_forms.layout import Submit
from crispy_forms.helper import FormHelper
from django import forms
from blog.models import Comment, Tag, Post

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['value']
        
    def __init__(self, *args, **kwargs):
        super(TagForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))
        
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ["content"]

  def __init__(self, *args, **kwargs):
    super(CommentForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.add_input(Submit('submit', 'Submit'))
    
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['published_at', 'title', 'slug', 'summary', 'content', 'tags']
        widgets = {
            'published_at': forms.DateInput(format=('%m/%d/%Y'), attrs={'class': 'form-control',
                'placeholder': 'Select a published date',
                'type': 'date'
            }),
        }
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', 'Submit'))