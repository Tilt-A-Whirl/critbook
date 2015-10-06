from django.conf.urls import url 

from . import views

urlpatterns = [
	# ex: /critbook/
	url(r'^$', views.index, name='index'),
	# ex: /critbook/5/
	url(r'^(?P<critique_id>[0-9]+)/$', views.notes, name='notes'),
	# ex: /about/
	url(r'^about', views.about, name='about'),
] 