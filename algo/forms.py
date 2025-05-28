from about.models import Manager
from .models import Calc

from django import forms
from django.forms import ModelForm, TextInput, Textarea, FileInput, IntegerField


class ManagerForm(ModelForm):
    class Meta:
        model = Manager
        fields = ['fio', 'image', 'html_block']

        widgets = {
            'fio': TextInput(attrs={'class': 'fio', 'placeholder': "ФИО",}),
            'image': FileInput(attrs={'class': 'image', 'type': 'file', 'accept': "image/*"}),
            'html_block': Textarea(attrs={'class': 'html_block', 'placeholder': 'HTML BLOCK'})
        }

class CalcForm(ModelForm):
    class Meta:
        model = Calc
        fields = ['a']

        widgets = {
            'a': TextInput(attrs={'class': 'a', 'placeholder': "Введите натуральное число",}),
        }



class CalcFilterForm(forms.Form):
    min_value = forms.IntegerField(label="Минимальное значение A", required=False, widget=forms.NumberInput(attrs={'placeholder': 'От'}))

class CalcFilterFormX(forms.Form):
    min_value_x = forms.IntegerField(label="Минимальное значение X", required=False, widget=forms.NumberInput(attrs={'placeholder': 'От'}))

class CalcSortedForm(forms.Form):
    variant = forms.ChoiceField(label="Сортировка", required=False, choices=[['-a', 'Наибольшее А'], ['-x', 'Наибольшее X'], ['a', 'Наименьшее А'], ['x', 'Наименьшее X']])