__author__ = 'woongkaa'
from django.http import JsonResponse
from django.db.models import QuerySet, Model
from dashboard.models import DailyLog, AdDailyTbl, AdTbl
from django.forms import model_to_dict

def model_json_response(model_instance):
    return JsonResponse(model_to_dict(model_instance))

def qs_json_response(queryset):
    json_list = []

    # if isinstance(queryset.first(), DailyLog):
    if isinstance(queryset.first(), AdDailyTbl):
        for instance in queryset:
            json_list.append({
                # 'date': str(instance.date.date()),
                'date' : instance.date,
                'v_count': instance.ad_hit,
                'uv_count': instance.uv_hit,
                'p_count': instance.post_count,
            })
    elif isinstance(queryset.first(), DailyLog):
        for instance in queryset:
            json_list.append({
                'date': str(instance.date.date()),
                # 'date' : instance.date,
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
            return qs_json_response(response)
        elif isinstance(response, Model):
            return model_json_response(response)
        return response