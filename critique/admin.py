from django.contrib import admin

from .models import Critique, Note

# Inline notes for critique
class NoteInline(admin.TabularInline):
	fields = ['text', 'pos_x', 'pos_y']
	model = Note
	extra = 1

class CritiqueAdmin(admin.ModelAdmin):
	inlines = [NoteInline]

admin.site.register(Critique, CritiqueAdmin)