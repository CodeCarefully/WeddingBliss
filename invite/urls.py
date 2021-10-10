from django.urls import path
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.HomepageView.as_view(), name='index'),
    re_path(r'^w/(?P<wed_slug>\w+)/$', views.WeddingView.as_view(), name='weddinghome'),
    re_path(r'^w/(?P<wed_slug>\w+)/invite$', views.InviteView.as_view(), name='invite'),
]