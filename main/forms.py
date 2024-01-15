from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Представьтесь, пожалуйста', 'class': 'form-control'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'example@domain.com', 'class': 'form-control'}
        )
    )
    phone = forms.CharField(
        min_length=9,
        widget=forms.TextInput(
            attrs={'placeholder': '+375 (12) 345-67-89', 'class': 'form-control'}
        )
    )
