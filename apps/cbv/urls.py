from django.conf.urls import url
from . import views

app_name = 'apps/cbv'

urlpatterns = [
	url(r'^$', views.SchoolListView.as_view(), name='list'),
	# grab the cbv app /primarykey and take that in as SchoolDetailView
	url(r'^(?P<pk>\d+)/$', views.SchoolDetailView.as_view(), name='detail'),
	url(r'^create/$', views.SchoolCreateView.as_view(), name='create'),
	url(r'^update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(), name='update'),
	url(r'^delete/(?P<pk>\d+)/$', views.SchoolDeleteView.as_view(), name='delete'),
]