
from django.db import models
from mongoengine import *

connect('import', host='127.0.0.1', port = 27017)

# Create your models here.
class PriceHistory(Document):
    #city = StringField()
    city_name = StringField()
    area = StringField()
    year = StringField()
    month = StringField()
    price = StringField()
    trendency = StringField()

    meta = {
        "collection" : "JS_suzhou",
    }

