from django.db import models

# Create your models here.
from mongoengine import *


connect('houseprice', host='127.0.0.1', port = 27017)

# Create your models here.
class House(Document):
    name = StringField()
    district_main = StringField()
    district_second = StringField()
    location = StringField()
    status = StringField()
    main_price = StringField()
    second_price = StringField()
    area = StringField()
    lng = FloatField()
    lat = FloatField()

    meta={'collection':'suzhou'}