from datetime import date

from django import forms

# from django.utils import timezone
from ToDo_app1.models import Todo


class DateInput(forms.DateInput):
    input_type = 'date'  # input type should be date


class ToDoForm(forms.ModelForm):
    date = forms.DateField(widget=DateInput)  # set the form field to date field & assign to the model field name itself

    class Meta:
        model = Todo
        fields = ('title', 'task', 'date',)
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter the title'}),
            'task': forms.TextInput(attrs={'placeholder': 'Enter the task'})
        }

    def check_date(self):
        date1 = self.cleaned_data['date']
        today = date.today()

        if date1 < today:
            # raise forms.ValidationError("Due date cannot be in the past!")
            self.add_error('date', "Due date cannot be in the past!")
        return date1

    def clean(self):
        cleaned_data = super().clean()
        self.check_date()
