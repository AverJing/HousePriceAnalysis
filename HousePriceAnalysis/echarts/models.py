from django.db import models
from mongoengine import *

#connect('lianjia', host='127.0.0.1', port = 27017)
connect('lianjia', host='mongodb://housepricedata:22kWqyxYCbP4HgMvmUSyb7ciZ6l002uZGYl9QVT35d3CwN437u9vlcv3Gp9E47KQwco5DpUI1fEhhLeFfWUFXQ==@housepricedata.documents.azure.cn:10255/?ssl=true&replicaSet=globaldb')

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