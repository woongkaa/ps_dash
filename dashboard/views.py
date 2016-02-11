# coding=utf-8
from django.shortcuts import render
from django.conf import settings
from django.views.generic import View, DetailView, TemplateView
from dashboard.models import *
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse

# Create your views here.
class MovieListJson(View):
    def get(self, request):
        return AdTbl.objects.all()


class MoviesRecent(View):
    def get(self, request):
        return AdTbl.objects.order_by('-ad_key')[:15]


class MovieInfo(View):
    def get(self, request, **kwargs):
        return AdTbl.objects.filter(ad_key=kwargs['pk'])


def json_movie_info(request, **kwargs):
    return AdTbl.objects.filter(ad_key=kwargs['pk'])


class Monitoring(View):
    def get(self, request, **kwargs):
        row_movie = json_movie_info(request, **kwargs)[0]
        return HttpResponse(str(row_movie.ad_key) + ' ' + row_movie.ad_title)


def movie_detail(request):
    row = AdTbl.objects.get(ad_key=request.GET['pk'])
    result = {'pk': row.ad_key, 'title': row.ad_title}
    return JsonResponse(result)


def monitoring(request, **kwargs):
    movie = AdTbl.objects.get(ad_key=kwargs['pk'])
    logs = DailyLog.objects.filter(movie=kwargs['pk'])
    return render(request, "dashboard/monitor.html", {'movie':movie,'logs':logs})