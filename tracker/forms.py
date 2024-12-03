from django import forms
from .models import Habit, HabitLog
from datetime import date
from django.core.exceptions import ValidationError

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ("name", "description")

class HabitLogForm(forms.ModelForm):
    class Meta:
        model = HabitLog
        fields = ("date", "status")
    
    def clean_date(self):
        date_value = self.cleaned_data.get('date')
        if date_value and date_value <= date.today():
            raise ValidationError("The date must be in the future")
        return date_value