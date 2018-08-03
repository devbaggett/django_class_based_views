from django.contrib import admin
from django.conf.urls import url, include
from apps.cbv import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.IndexView.as_view()),
    url(r'^cbv/', include('apps.cbv.urls', namespace='cbv'))
]
