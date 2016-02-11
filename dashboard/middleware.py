__author__ = 'woongkaa'
from django.http import JsonResponse
from django.db.models import QuerySet

def json_response(queryset):
    json_list = []
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