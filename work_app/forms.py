from django import forms
from django.core.exceptions import ValidationError


class MathForm(forms.Form):
    numbers = forms.CharField()

    def clean_numbers(self):
        numbers = self.cleaned_data['numbers']
        print(numbers)
        if not all(number.isdigit() for number in numbers.split()):
            raise ValidationError('Невірний формат вводу')
        return numbers