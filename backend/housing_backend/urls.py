from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from housing_backend import views

urlpatterns = [
    url(r'^affordable/$', views.AffordableList.as_view()),
    url(r'^affordable/(?P<pk>[0-9]+)/$', views.AffordableDetail.as_view()),
    url(r'^rent/$', views.RentList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
