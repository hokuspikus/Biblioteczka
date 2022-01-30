from django import forms
from django.core.exceptions import ValidationError

from bib_app.models import Author


def check_year(value):
    if value < 1000:
        raise ValidationError("Nie było wydawnictw przed 1000 rokiem")


def check_if_slawomir(value):
    a = ['slawek', 'kasia', 'gosia', 'martyna']
    if value in a:
        raise ValidationError("Tego człowieka nie obsługujemy")


def check_year_2(value):
    if value > 3000:
        raise ValidationError("naprawde ?? ")


class AddPublisherForm(forms.Form):
    name = forms.CharField(validators=[check_if_slawomir])
    year = forms.IntegerField(validators=[check_year, check_year_2])

    def clean(self):
        data = super().clean()
        name = data.get('name')
        year = data.get('year')
        if name == 'slawomir' and year < 1500:
            raise ValidationError("nie moze to być!!!")
        return data


class AddBookForm(forms.Form):
    title = forms.CharField()
    author = forms.ModelChoiceField(queryset=Author.objects.all())



