from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User
from django.contrib.auth import get_user_model

class CustumUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User

class CustumUserChangForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email','first_name','last_name',)