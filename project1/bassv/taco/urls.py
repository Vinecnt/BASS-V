from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^courses/$', views.CourseListView.as_view(), name='courses'),
    url(r'^course/(?P<pk>\d+)$', views.CourseDetailView.as_view(), name='course-detail'),
    url(r'^messages/$', views.MessageListView.as_view(), name='messages'),
    url(r'^ta/$', views.TAListView.as_view(), name='ta'),
]
