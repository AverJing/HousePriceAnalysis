# coding:utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client["HousePriceHistory"]
col = db.get_collection("BigCitys_chongqing")  # 找到该城市的集合名
datas = col.find({"year":"2019","month":"03"}, {"_id": 0, "city_name":1,"area": 1})  # 查找该城市的所有区域

citys = []  # 存放城市名
areas = [] # 存放对应城市的区域名
for data in datas:
    #print(data)
    area = data.get('area')
    if area == "1":
        #area = "市辖区"
        continue
    #print(area)
    areas.append(area)

#for area in areas:
#    print(area)
print(areas)