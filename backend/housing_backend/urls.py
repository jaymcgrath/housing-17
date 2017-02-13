from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from housing_backend import views

urlpatterns = [
    url(r'^affordable/$', views.AffordableList.as_view(), name='affordable_list'),
    url(r'^affordable/(?P<pk>[0-9]+)/$', views.AffordableDetail.as_view(), name='affordable_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
