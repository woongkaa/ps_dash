# -*- coding: utf-8 -*-
__author__ = 'woongkaa'
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from dashboard.models import AdTbl, AdDailyTbl, DailyLog



@admin.register(AdTbl)
class MovieAdmin(admin.ModelAdmin):
    # list_display = ['ad_title']
    search_fields = ['ad_title']
    # fields = (('ad_title', 'ad_key'), 'income')


@admin.register(DailyLog)
class MovieLogAdmin(admin.ModelAdmin):
    search_fields = ['movie']
    fieldsets = (
        (None,{
            'fields' : ('date', 'movie', 'ad_hit', 'uv_hit', 'post_count')
        }),
    )
    list_display = ('date_only', 'movie', 'ad_hit', 'uv_hit', 'post_count')
    list_display_links = ('date_only', 'movie', 'ad_hit', 'uv_hit', 'post_count')
    ordering = ('-date',)

    def date_only(self, obj):
        return obj.date.strftime("%y-%m-%d")

    date_only.short_description = '추가된 날짜'
