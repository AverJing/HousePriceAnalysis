from __future__ import unicode_literals

from django.shortcuts import render
from .models import House
from mongoengine import *
import json


def show_map(request):
    districts = ["吴中", "姑苏", "吴江", "相城", "昆山"]
    avg_price = get_data(districts)
    json_data = {
        'avg_price': json.dumps(avg_price),
        'area': json.dumps(districts)
    }
    return render(request, 'app1/map.html', json_data)


def get_data(districts):
    connect('houseprice')
    avg_price = []
    i = 0
    for d in districts:
        count = 0
        houses = House.objects()
        print(houses)
        avg = 0
        for h in houses:
            avg += int(h.main_price)
            count += 1
        if count != 0:
            avg /= count
        avg_price.append(avg)
        i += 1
    return avg_price


