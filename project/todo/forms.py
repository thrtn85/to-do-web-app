from django import forms
from .models import ToDo


class ToDoForm(forms.ModelForm):
	task = forms.CharField(max_length=100)

	class Meta:
		model = ToDo
		fields = ['task',]
