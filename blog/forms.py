from django.forms import ModelForm
from .models import Comment

##### POST COMMENT FORM #####

class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('name', 'email', 'your_comment')