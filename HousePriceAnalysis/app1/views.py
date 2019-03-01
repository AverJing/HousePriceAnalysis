from __future__ import unicode_literals

from django.shortcuts import render
import json


def china_map(request, china):
    data = []
    json_data = {
        'map_name': json.dumps(china),
        'map_level': json.dumps(1),
        'data': json.dumps(data),
    }
    return render(request, 'app1/map.html', json_data)


def province_map(request, china, province):
    data = []
    json_data = {
        'map_name': json.dumps(province),
        'map_level': json.dumps(2),
        'data': json.dumps(data),
    }
    return render(request, 'app1/map.html', json_data)


def city_map(request, china, province, city):
    data = []
    json_data = {
        'map_name': json.dumps(city),
        'map_level': json.dumps(3),
        'data': json.dumps(data),
    }
    return render(request, 'app1/map.html', json_data)


