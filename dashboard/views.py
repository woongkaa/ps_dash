# coding=utf-8
from django.shortcuts import render
from django.conf import settings
from django.views.generic import View, DetailView, TemplateView
from dashboard.models import *
from django.core.urlresolvers import reverse
from django.http import HttpResponse, JsonResponse

# Create your views here.
def json_movie_info(request, **kwargs):
    try:
        qs = AdTbl.objects.filter(ad_key=kwargs['pk'])
    except ObjectDoesNotExist:
        qs = None
    return qs


def json_movie_log(request, **kwargs):
    try:
        # qs = DailyLog.objects.filter(movie=kwargs['pk'])
        qs = AdDailyTbl.objects.filter(ad_key=kwargs['pk'])
    except ObjectDoesNotExist:
        qs = None
    return qs


def movie_detail(request):
    row = AdTbl.objects.get(ad_key=request.GET['pk'])
    result = {'pk': row.ad_key, 'title': row.ad_title}
    return JsonResponse(result)


def monitoring(request, **kwargs):
    movie = AdTbl.objects.get(ad_key=kwargs['pk'])
    logs = DailyLog.objects.filter(movie=kwargs['pk'])
    return render(request, "dashboard/monitor.html", {'movie':movie,'logs':logs})


class Dashboard(DetailView):
    template_name = "dashboard/index.html"
    model = AdTbl

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        return context


class MovieLog(View):
    def get(self, request, **kwargs):
        try:
            # qs = DailyLog.objects.filter(movie=kwargs['pk'])
            qs = AdDailyTbl.objects.filter(ad_key=kwargs['pk'])
        except ObjectDoesNotExist:
            qs = None
        return qs


class MovieInfo(View):
    def get(self, request, **kwargs):
        try:
            instance = AdTbl.objects.get(ad_key=kwargs['pk'])
        except ObjectDoesNotExist:
            instance = None
        return instance


class Monitoring(View):
    def get(self, request, **kwargs):
        row_movie = json_movie_info(request, **kwargs)[0]
        return HttpResponse(str(row_movie.ad_key) + ' ' + row_movie.ad_title)


class TestView(TemplateView):
    template_name = "dashboard/index.html"