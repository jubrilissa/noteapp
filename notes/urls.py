from django.conf.urls import url
from notes import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'notesapi$', views.NoteListView.as_view(), name='list_note'),
    url(r'^notesapi/(?P<pk>[0-9]+)/$', views.NoteDetailView.as_view(), name='single_note'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
