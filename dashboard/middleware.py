__author__ = 'woongkaa'
from django.http import JsonResponse
from django.db.models import QuerySet
from dashboard.models import DailyLog

def json_response(queryset):
    json_list = []

    if isinstance(queryset.first(), DailyLog):
        for instance in queryset:
            json_list.append({
                'date': str(instance.date.date()),
                'v_count': instance.ad_hit,
                'uv_count': instance.uv_hit,
                'p_count': instance.post_count,
            })
    else:
        for instance in queryset:
            json_list.append({
                'id': instance.ad_key,
                'title': instance.ad_title,
            })

    return JsonResponse(json_list, safe=False)

class JsonResponseMiddleware(object):
    def process_response(self, request, response):
        if isinstance(response, QuerySet):
            return json_response(response)
        return response