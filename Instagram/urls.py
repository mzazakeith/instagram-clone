from django.conf.urls import url,include
from django.contrib.auth import views
    url(r'^',include('mzazagram.urls')),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^logout/$', views.logout, {"next_page":'/accounts/login'}),
]
