from django.conf.urls import url
from . import views

urlpatterns = [
  url(r'^$', views.greeting, name='greeting'),
  url(r'^hair_color_detail/(?P<pk>\d+)/$', views.hair_color_detail, name='hair_color_detail'),
]