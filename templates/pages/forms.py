from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from book.models import book

class CustomUserCreationForm(UserCreationForm):
    class Meta: 
      # fields = "__all__"
      fields = ['first_name','last_name']
      model = User

class AddBookForm(ModelForm):
   class Meta:
      fields = "__all__"
      model = book