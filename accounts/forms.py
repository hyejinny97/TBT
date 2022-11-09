from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomCreationUserForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = [
            'username',
            'nickname',
            'email',
            'profile_image'         
        ]

        labels = {
            'username' : '이름',
            'nickname' : '닉네임',
            'email' : '이메일',
            'profile_image' : '프로필 사진',
        }

class CustomChangeUserForm(UserChangeForm):
    password = None
    model = get_user_model()
    fields = [
            'username',
            'nickname',
            'email',
            'profile_image'         
        ]

    labels = {
            'username' : '이름',
            'nickname' : '닉네임',
            'email' : '이메일',
            'profile_image' : '프로필 사진',
        }
