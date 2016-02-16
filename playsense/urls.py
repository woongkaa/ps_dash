"""playsense URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from dashboard import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^movie_detail.json/(?P<pk>[0-9]+)$',views. MovieInfo.as_view(), name="movie_detail"),
    url(r'^movie_log.json/(?P<pk>[0-9]+)$', views.MovieLog.as_view(), name="movie_log"),
    url(r'^monitoring/(?P<pk>[0-9]+)$', views.Monitoring.as_view(), name="monitoring"),
    url(r'^movie$', views.movie_detail,name="movie"),
    url(r'^monitorf/(?P<pk>[0-9]+)$', views.monitoring, name="monitoring_fbv"),
    url(r'^dashboard/', include("dashboard.urls")),
    url(r'^testboard$', views.TestView.as_view(), name="dash_test"),
]
