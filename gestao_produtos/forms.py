from django.forms import ModelForm
from django.contrib.auth.models import User
from home.models import Comment

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']