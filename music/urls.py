from django.conf.urls import url
from . import views
app_name='music'
urlpatterns = [
	# /music/
	url(r'^$', views.IndexView.as_view(), name='index'),

	# /music/712/
	url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

	#/music/album/add/
	url(r'^album/add/$',views.AlbumCreate.as_view(),name='album-add'),

	#/music/album/<pk>/
	url(r'^album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name='album-update'),

	#/music/album/<pk>/delete
	url(r'^album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name='album-delete'),

	#/music/song/add/
	url(r'^song/add/$',views.SongCreate.as_view(),name='song-add'),

	#/music/song/<pk>/
	url(r'^song/(?P<pk>[0-9]+)/$',views.SongUpdate.as_view(),name='song-update'),

	#/music/song/<pk>/delete
	url(r'^song/(?P<pk>[0-9]+)/delete/$',views.SongDelete.as_view(),name='song-delete'),

	url(r'^register/$', views.UserFormView.as_view(), name='register'),
]