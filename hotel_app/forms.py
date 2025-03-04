from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Room

class RegisterForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RoomForm(forms.ModelForm):
    occupant_name = forms.CharField(widget=forms.TimeInput(attrs={'class': 'form-control'}), required=False)
    room_number = forms.IntegerField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
    bed_type = forms.ChoiceField(
        choices=Room.BED_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    smoking = forms.ChoiceField(
        choices=Room.SMOKING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    rate = forms.DecimalField(widget=forms.TimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Room
        fields = ['occupant_name','room_number', 'bed_type', 'smoking', 'rate']


class RoomUpdateForm(forms.ModelForm):
    occupant_name = forms.CharField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
    bed_type = forms.ChoiceField(
        choices=Room.BED_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    smoking = forms.ChoiceField(
        choices=Room.SMOKING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    rate = forms.DecimalField(widget=forms.TimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Room
        fields = ['occupant_name', 'bed_type', 'smoking', 'rate']

class RoomCreateForm(forms.ModelForm):
    room_number = forms.IntegerField(widget=forms.TimeInput(attrs={'class': 'form-control'}))
    bed_type = forms.ChoiceField(
        choices=Room.BED_TYPE_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    smoking = forms.ChoiceField(
        choices=Room.SMOKING_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    rate = forms.DecimalField(widget=forms.TimeInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Room
        fields = ['room_number', 'bed_type', 'smoking', 'rate']