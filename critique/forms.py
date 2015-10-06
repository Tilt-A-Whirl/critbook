from django import forms

from .models import *

class CritiqueNewForm(forms.ModelForm):
	""" New critique form 
	"""
	class Meta:
		model = Critique
		fields = ['title']
		widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Enter a title'}),
        }

	def process(self):
		cd = self.cleaned_data
		c = Critique(title=cd['title'])
		c.save()
		return c

class CritiqueEditForm(forms.ModelForm):
	""" Form to edit critique title or delete 
	"""
	class Meta:
		model = Critique
		fields = ['title']
		widgets = {
            'title': forms.TextInput(attrs={'class': 'hidden'}),
        }

class ImageForm(forms.ModelForm):
	""" Form to upload or replace critique image 
	"""
	class Meta:
		model = Critique
		fields = ['image_file']

class NoteNewForm(forms.ModelForm):
	""" New note form 
	"""
	class Meta:
		model = Note
		fields = ['text']
		widgets = {
            'text': forms.Textarea(attrs={'placeholder': 'Enter a note', 'rows': 3}),
        }

	def process(self, critique_id):
		cd = self.cleaned_data
		n = self.save(commit=False)
		n.critique_id = critique_id
		n.save()

class NoteEditForm(forms.ModelForm):
	""" Form to edit a note or delete 
	"""
	class Meta:
		model = Note
		fields = ['critique', 'text', 'isCompleted', 'pos_x', 'pos_y']
		widgets = {
            'isCompleted': forms.CheckboxInput(attrs={'required': False, 'class': 'complete'}),
            'text': forms.Textarea(attrs={'class': 'hidden', 'rows': 3}),
        }
	