from django.conf.urls import include, url
from dashboard import views

urlpatterns = [
    url(r'(?P<pk>[0-9]+)$', views.Dashboard.as_view(), name="dashboard"),
    # url(r'(?P<pk>[0-9]+)/chart.json$', views.json_movie_log, name="chart_data"),
]
