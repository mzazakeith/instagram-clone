from django.conf.urls import url
from . import views
from . import email
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name = 'home'),
    url(r'^signup/$', email.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',email.activate, name='activate'),
    url(r'^new/image$', views.upload, name='new-image'),
    url(r'^profile$', views.profile, name='myprofile'),
    url(r'^explore$', views.explore, name='explore'),
    url(r'^userprofile/(?P<user_id>\d+)',views.userprofile,name = 'profile'),
    url(r'follow/(?P<user_id>\d+)', views.follow, name='follow'),
    url(r'^new/profile$', views.create_profile, name='new-profile'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^comment/(?P<image_id>\d+)',views.comment, name='comment')


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
