from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect

from .models import Critique, Note
from .forms import *

def index(request):
	""" Index view
	"""
	new_form = None
	edit_forms = None
	#if this is a POST request we need to process the form data
	if request.method == 'POST':
		# if this comes from the new critique form:
		if request.POST.get('new_critique'):
			# create a form instance and populate it with data from the request:
			new_form = CritiqueNewForm(request.POST)
			# check whether it's valid:
			if new_form.is_valid():
				# process the data in form.cleaned_data as required:
				c = new_form.process()
				# redirect to a new URL:
				return HttpResponseRedirect('.')

		# if it comes from an edit form:
		else:
			critique_id = request.POST.get('critique_id')
			edited_critique = get_object_or_404(Critique, pk=critique_id)
			# if the delete box is checked, delete the instance:
			if request.POST.get('delete'):
				edited_critique.delete()
			# otherwise update it:
			else:
				edit_form = CritiqueEditForm(request.POST, request.FILES, instance=edited_critique)
				# check whether it's valid:
				if edit_form.is_valid():
					# process the data in form.cleaned_data as required:
					edit_form.save()
					# redirect to a new URL:
					return HttpResponseRedirect('.')

	# if a GET (or any other method) we'll create blank forms
	if new_form is None:
		new_form = CritiqueNewForm()
	if edit_forms is None:
		edit_forms = []
		for critique in Critique.objects.all():
			edit_form = CritiqueEditForm(instance=critique, auto_id=False)
			edit_forms.append(edit_form)
	num_critiques = Critique.objects.all().count
	context = {'new_form': new_form, 'edit_forms': edit_forms, 'num_critiques': num_critiques}
	return render(request, 'critique/index.html', context)

def notes(request, critique_id):
	""" Notes view
	"""
	critique = get_object_or_404(Critique, pk=critique_id)
	critique_list = Critique.objects.all()
	max_notes = 26
	new_form = None
	image_form = None
	edit_forms = None
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# if this comes from the new note form:
		if request.POST.get('new_note'):
			# create a form instance and populate it with data from the request:
			new_form = NoteNewForm(request.POST)
			# check whether it's valid:
			if new_form.is_valid():
				# process the data in form.cleaned_data as required:
				new_form.process(critique_id)
				# redirect to a new URL:
				return HttpResponseRedirect('.')
		# otherwise if this comes from the image uploader:
		elif request.FILES.get('image_file'):
			# create an image form instance and populate it:
			image_form = ImageForm(request.POST, request.FILES, instance=critique)
			# check whether it's valid:
			if image_form.is_valid():
				# save the critique with the image:
				image_form.save()
				# redirect:
				return HttpResponseRedirect('.')
		# otherwise this is an edited note:
		else:
			# create a form instance and populate it with data from the request:
			note_id = request.POST.get('note_id')
			edited_note = get_object_or_404(Note, pk=note_id)
			# if we're deleting this note:
			if request.POST.get('delete'):
				edited_note.delete()
			# otherwise update the instance:
			else:
				edit_form = NoteEditForm(request.POST, instance=edited_note)
				# check whether it's valid:
				if edit_form.is_valid():
					# save the updated instance:
					edit_form.save()
					# redirect to a new URL:
					return HttpResponseRedirect('.')

	# if a GET (or any other method) we'll create blank forms
	if new_form is None:
		new_form = NoteNewForm()
	if image_form is None:
		image_form = ImageForm(instance=critique)
	if edit_forms is None:
		edit_forms = []
		for note in critique.note_set.all():
			edit_form = NoteEditForm(instance=note, auto_id=False)
			edit_forms.append(edit_form)
	context = {
		'critique': critique, 
		'new_form': new_form, 
		'image_form': image_form,
		'edit_forms': edit_forms, 
		'max_notes': max_notes, 
		'critique_list': critique_list,
		}
	return render(request, 'critique/notes.html', context)

def about(request):
	""" About view
	"""
	critique_list = Critique.objects.all()
	context = {
		'critique_list': critique_list,
		}
	return render(request, 'critique/about.html', context)
