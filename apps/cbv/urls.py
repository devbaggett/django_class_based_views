from django.conf.urls import url
from . import views

app_name = 'apps/cbv'

urlpatterns = [
	url(r'^$', views.SchoolListView.as_view(), name='list'),
	# grab the cbv app /primarykey and take that in as SchoolDetailView
	url(r'^(?P<pk>[-\w]+)/$', views.SchoolDetailView.as_view(), name='detail')
]