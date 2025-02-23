from django.contrib.auth.forms import UserCreationForm
from django import forms

from users.models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    phone_number = forms.CharField(max_length=15, required=False,
                                   help_text='Необязательное поле. Введите ваш номер телефона.')

    class Meta:
        model = CustomUser
        fields = ('email', 'phone_number', 'username', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = 'Обязательно поле. 150 символов или менее. Только буквы, цифры и @/./+/-/_ '
        self.fields['first_name'].help_text = 'Необязательное поле. Введите ваше имя'
        self.fields['last_name'].help_text = 'Необязательное поле. Введите вашу фамилию'
        self.fields['password2'].help_text = 'Введите такой же пароль, что и ранее для проверки подлинности личности'
        self.fields['password2'].label = 'Confirm password'

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and not phone_number.isdigit():
            raise forms.ValidationError('Номер телефона должен состоять только из цифр')
        return phone_number
