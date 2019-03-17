
from django.db import models
from mongoengine import *

#connect('import', host='127.0.0.1', port = 27017)
connect('yearPriceData', host='mongodb+srv://averjing:Fu.ture1@housepriceanalysis-7vvvm.azure.mongodb.net/test?retryWrites=true')

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

