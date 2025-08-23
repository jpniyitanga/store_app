from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account, Address


class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['street', 'city']


class CustomUserCreationForm(UserCreationForm):
    street = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)

    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name',
                  'last_name', 'password1', 'password2',  'street', 'city')

    def save(self, commit=True):
        address = Address(
            street=self.cleaned_data['street'],
            city=self.cleaned_data['city']
        )
        address.save()

        user = super().save(commit=True)
        user.default_address = address
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Account
        fields = ('email', 'username', 'first_name',
                  'last_name', 'default_address')
