# coding:utf-8
import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client["HousePriceHistory"]
col = db.get_collection("A_New")  # 找到该城市的集合名
datas = col.find({}, {"_id": 0, "province":1,"city_name":1,"area": 1})  # 查找该城市的所有区域
provinces = []  # 存放省份的名字

citys = []  # 存放对应省份的城市名

areas = [] # 存放对应城市的区域名
for data in datas:
    #print(data) #{'city_name': '六盘水', 'area': '六盘水周边', 'province': '贵州'}
    #print(data.get('province'))
    province = data.get('province')
    if province not in provinces:
        provinces.append(province)
print(len(provinces))
for province in provinces:
    print("{name:'"+province+"',cityList:[")
    city_data = col.find({"province":province,"area":"1"},{"_id":0,"city_name":1})
    for city in city_data:
        city_name = city.get('city_name')
        #print(city_name)
        citys.append(city_name)
        #print("name:'",city_name,"市',areaList:")
        area_data = col.find({"province":province,"city_name":city_name,},{"_id":0,"area":1})
        for area in area_data:
            area_name = area.get('area')
            if area_name == "1":
                area_name = "市辖区"
            areas.append(area_name)
        print("{name:'"+city_name+"市',areaList:",areas,"},")
        #print(areas)
        areas = []
    print("]},")
    #print("市辖区",citys)
    citys = []

