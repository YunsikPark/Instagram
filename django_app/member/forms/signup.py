from django import forms
from django.contrib.auth import get_user_model
from django.http import HttpResponse

User = get_user_model()


class SignupForm(forms.Form):
    # SignupForm을 구성하고 해당 form을 view에서 사용하도록 설정
    username = forms.CharField(
        max_length=20,
        help_text= 'Signup help text test',
        widget=forms.TextInput(
            attrs={
                'placeholder': '사용할 아이디를 입력하세요',
            }
        )
    )
    nickname = forms.CharField(
        max_length=24,
        help_text= '닉네임은 유일해야 합니다.',
        widget=forms.TextInput(
            attrs={
                'placeholder': '사용할 닉네임을 입력하세요',
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 입력하세요',
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': '비밀번호를 다시한번 입력하세요',
            }
        )
    )

    # clean_<fieldname>메서드를 사용해서
    # username필드에 대한 유효성 검증을 실행
    def clean_username(self):
        username = self.cleaned_data.get('username')
        if username and User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                'Username already exist'
            )
        return username

    def clean_nickname(self):
        nickname = self.cleaned_data.get('nickname')
        if nickname and User.objects.filter(nickname=nickname).exists():
            raise forms.ValidationError(
                'Nickname already exist'
            )

    def clean_password2(self):
        # password1과 비교하여 같은지
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'Password mismatched',
            )
        return password2

    def create_user(self):
        # 자신의 cleaned_data를 사용해서 유저를 생성
        # 생성한 유저를 반환
        username = self.cleaned_data['username']
        password = self.cleaned_data['password2']
        user = User.objects.create_user(
            username=username,
            password=password
        )
        return user
