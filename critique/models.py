from django.db import models
from django.dispatch import receiver

import os

class Critique(models.Model):
	""" Critique model. Includes title, image, and image
		width and height. 
	"""
	title = models.CharField(max_length=50)
	width = models.IntegerField(default=0, blank=True)
	height = models.IntegerField(default=0, blank=True)
	image_file = models.ImageField(upload_to='crit_images/%Y/%m/%d', 
		height_field='height', 
		width_field='width', 
		max_length=200,
		blank=True)

	def __unicode__(self):
		return self.title

class Note(models.Model):
	""" Note model. Belongs to one critique and Includes
		coordinates for positioning associated image 
		labels. 
	"""
	critique = models.ForeignKey(Critique)
	text = models.CharField(max_length=250)
	pos_x = models.IntegerField('x position', default=0)
	pos_y = models.IntegerField('y position', default=0)
	isCompleted = models.BooleanField(default=False)

	def __unicode__(self):
		return self.critique.__unicode__() + " (" + str(self.id) + ")"

# These two auto-delete uploaded image files from filesystem when they are unneeded:
@receiver(models.signals.post_delete, sender=Critique)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """ Deletes file from filesystem when corresponding 
    	Critique object is deleted.
    """
    if instance.image_file:
        if os.path.isfile(instance.image_file.path):
            os.remove(instance.image_file.path)

@receiver(models.signals.pre_save, sender=Critique)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """ Deletes file from filesystem when corresponding 
    	Critique object is changed.
    """
    if not instance.pk:
        return False

    old_file = Critique.objects.get(pk=instance.pk).image_file
    if old_file:
	    new_file = instance.image_file
	    if not old_file == new_file:
	        if os.path.isfile(old_file.path):
	            os.remove(old_file.path)

