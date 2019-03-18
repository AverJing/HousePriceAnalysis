// 纯JS省市区三级联动
var addressInit = function(_cmbProvince, _cmbCity, defaultProvince, defaultCity)
{
	var cmbProvince = document.getElementById(_cmbProvince);
	var cmbCity = document.getElementById(_cmbCity);

	
	function cmbSelect(cmb, str)
	{
		for(var i=0; i<cmb.options.length; i++)
		{
			if(cmb.options[i].value == str)
			{
				cmb.selectedIndex = i;
				return;
			}
		}
	}
	function cmbAddOption(cmb, str, obj)
	{
		var option = document.createElement("OPTION");
		cmb.options.add(option);
		option.innerHTML = str;
		option.value = str;
		option.obj = obj;
	}
	
	function changeCity()
	{
		if(cmbCity.selectedIndex == -1)return;
		var item = cmbCity.options[cmbCity.selectedIndex].obj;

	}
	function changeProvince()
	{
		cmbCity.options.length = 0;
		cmbCity.onchange = null;
		if(cmbProvince.selectedIndex == -1)return;
		var item = cmbProvince.options[cmbProvince.selectedIndex].obj;
		for(var i=0; i<item.cityList.length; i++)
		{
			cmbAddOption(cmbCity, item.cityList[i].name, item.cityList[i]);
		}
		cmbSelect(cmbCity, defaultCity);
		changeCity();
		cmbCity.onchange = changeCity;
	}
	
	for(var i=0; i<provinceList.length; i++)
	{
		cmbAddOption(cmbProvince, provinceList[i].name, provinceList[i]);
	}
	cmbSelect(cmbProvince, defaultProvince);
	changeProvince();
	cmbProvince.onchange = changeProvince;
}


function changeProvince(_cmbProvince,_cmbCity)
	{
	    var cmbProvince = document.getElementById(_cmbProvince);
        var cmbCity = document.getElementById(_cmbCity);
		cmbCity.options.length = 0;
		cmbCity.onchange = null;
		if(cmbProvince.selectedIndex == -1)return;
		var item = cmbProvince.options[cmbProvince.selectedIndex].obj;
		for(var i=0; i<item.cityList.length; i++)
		{
			cmbAddOption(cmbCity, item.cityList[i].name, item.cityList[i]);
		}
		cmbSelect(cmbCity, defaultCity);
		changeCity();
		cmbCity.onchange = changeCity;
	}
var provinceList = [
{name:'一线城市',cityList:[
{name:'北京'},
{name:'上海'},
{name:'天津'},
{name:'重庆'}
]},
{name:'河北',cityList:[
{name:'石家庄市'},
{name:'秦皇岛市'},
{name:'承德市'},
{name:'衡水市'},
{name:'邯郸市'},
{name:'邢台市'},
{name:'廊坊市'},
{name:'张家口市'},
{name:'唐山市'},
{name:'定州市'},
{name:'沧州市'},
{name:'保定市'},
]},
{name:'广东',cityList:[
{name:'江门市'},
{name:'茂名市'},
{name:'韶关市'},
{name:'惠州市'},
{name:'汕尾市'},
{name:'潮州市'},
{name:'顺德市'},
{name:'东莞市'},
{name:'清远市'},
{name:'湛江市'},
{name:'深圳市'},
{name:'中山市'},
{name:'佛山市'},
{name:'河源市'},
{name:'云浮市'},
{name:'汕头市'},
{name:'阳春市'},
{name:'广州市'},
{name:'肇庆市'},
{name:'阳江市'},
{name:'揭阳市'},
{name:'梅州市'},
{name:'珠海市'},
{name:'台山市'},
]},
{name:'云南',cityList:[
{name:'丽江市'},
{name:'保山市'},
{name:'玉溪市'},
{name:'西双版纳市'},
{name:'德宏市'},
{name:'楚雄市'},
{name:'昭通市'},
{name:'普洱市'},
{name:'文山市'},
{name:'大理市'},
{name:'曲靖市'},
{name:'红河市'},
{name:'临沧市'},
{name:'昆明市'},
]},
{name:'广西',cityList:[
{name:'玉林市'},
{name:'崇左市'},
{name:'北海市'},
{name:'防城港市'},
{name:'柳州市'},
{name:'南宁市'},
{name:'贺州市'},
{name:'河池市'},
{name:'百色市'},
{name:'来宾市'},
{name:'梧州市'},
{name:'钦州市'},
{name:'桂林市'},
{name:'贵港市'},
]},
{name:'吉林',cityList:[
{name:'长春市'},
{name:'延边市'},
{name:'白城市'},
{name:'辽源市'},
{name:'松原市'},
{name:'四平市'},
{name:'白山市'},
{name:'通化市'},
]},
{name:'江苏',cityList:[
{name:'镇江市'},
{name:'连云港市'},
{name:'宿迁市'},
{name:'沭阳市'},
{name:'扬州市'},
{name:'常州市'},
{name:'无锡市'},
{name:'南京市'},
{name:'淮安市'},
{name:'泰州市'},
{name:'昆山市'},
{name:'南通市'},
{name:'盐城市'},
{name:'徐州市'},
{name:'苏州市'},
]},
{name:'内蒙古',cityList:[
{name:'呼伦贝尔市'},
{name:'赤峰市'},
{name:'锡林郭勒盟市'},
{name:'海拉尔市'},
{name:'乌兰察布市'},
{name:'呼和浩特市'},
{name:'乌海市'},
{name:'包头市'},
{name:'鄂尔多斯市'},
{name:'兴安盟市'},
{name:'通辽市'},
{name:'巴彦淖尔市市'},
]},
{name:'辽宁',cityList:[
{name:'丹东市'},
{name:'沈阳市'},
{name:'抚顺市'},
{name:'大连市'},
{name:'鞍山市'},
{name:'本溪市'},
{name:'朝阳市'},
{name:'辽阳市'},
{name:'阜新市'},
{name:'葫芦岛市'},
{name:'锦州市'},
{name:'盘锦市'},
{name:'铁岭市'},
{name:'营口市'},
{name:'瓦市'},
]},
{name:'安徽',cityList:[
{name:'宣城市'},
{name:'六安市'},
{name:'阜阳市'},
{name:'马鞍山市'},
{name:'池州市'},
{name:'安庆市'},
{name:'淮北市'},
{name:'淮南市'},
{name:'和县市'},
{name:'芜湖市'},
{name:'蚌埠市'},
{name:'巢湖市'},
{name:'滁州市'},
{name:'铜陵市'},
{name:'合肥市'},
{name:'合肥市'},
{name:'宿州市'},
{name:'黄山市'},
{name:'亳州市'},
]},
{name:'湖北',cityList:[
{name:'仙桃市'},
{name:'随州市'},
{name:'咸宁市'},
{name:'荆州市'},
{name:'十堰市'},
{name:'荆门市'},
{name:'恩施市'},
{name:'黄石市'},
{name:'鄂州市'},
{name:'天门市'},
{name:'襄阳市'},
{name:'武汉市'},
{name:'孝感市'},
{name:'宜昌市'},
]},
{name:'山西',cityList:[
{name:'忻州市'},
{name:'运城市'},
{name:'长治市'},
{name:'朔州市'},
{name:'阳泉市'},
{name:'晋中市'},
{name:'吕梁市'},
{name:'太原市'},
{name:'晋城市'},
{name:'临汾市'},
{name:'大同市'},
]},
{name:'浙江',cityList:[
{name:'义乌市'},
{name:'瑞安市'},
{name:'湖州市'},
{name:'台州市'},
{name:'乐清市'},
{name:'嘉兴市'},
{name:'衢州市'},
{name:'绍兴市'},
{name:'杭州市'},
{name:'金华市'},
{name:'宁波市'},
{name:'丽水市'},
{name:'温州市'},
{name:'舟山市'},
]},
{name:'贵州',cityList:[
{name:'黔东南市'},
{name:'黔南市'},
{name:'黔西南市'},
{name:'铜仁市'},
{name:'遵义市'},
{name:'贵阳市'},
{name:'安顺市'},
{name:'毕节市'},
{name:'六盘水市'},
]},
{name:'福建',cityList:[
{name:'莆田市'},
{name:'南平市'},
{name:'宁德市'},
{name:'龙岩市'},
{name:'漳州市'},
{name:'泉州市'},
{name:'福州市'},
{name:'厦门市'},
{name:'三明市'},
]},
{name:'山东',cityList:[
{name:'济南市'},
{name:'诸城市'},
{name:'德州市'},
{name:'菏泽市'},
{name:'枣庄市'},
{name:'东营市'},
{name:'淄博市'},
{name:'莱芜市'},
{name:'潍坊市'},
{name:'临沂市'},
{name:'滨州市'},
{name:'泰安市'},
{name:'烟台市'},
{name:'青岛市'},
{name:'日照市'},
{name:'威海市'},
{name:'章丘市'},
{name:'聊城市'},
{name:'济宁市'},
]},
{name:'黑龙江',cityList:[
{name:'大庆市'},
{name:'绥化市'},
{name:'牡丹江市'},
{name:'牡丹江市'},
{name:'佳木斯市'},
{name:'齐齐哈尔市'},
{name:'伊春市'},
{name:'鸡西市'},
{name:'大兴安岭市'},
{name:'鹤岗市'},
{name:'七台河市'},
{name:'哈尔滨市'},
{name:'双鸭山市'},
]},
{name:'河南',cityList:[
{name:'开封市'},
{name:'商丘市'},
{name:'鹤壁市'},
{name:'周口市'},
{name:'长葛市'},
{name:'焦作市'},
{name:'新乡市'},
{name:'洛阳市'},
{name:'禹州市'},
{name:'郑州市'},
{name:'济源市'},
{name:'濮阳市'},
{name:'三门峡市'},
{name:'信阳市'},
{name:'驻马店市'},
{name:'漯河市'},
{name:'许昌市'},
{name:'安阳市'},
{name:'平顶山市'},
{name:'南阳市'},
]},
{name:'陕西',cityList:[
{name:'宝鸡市'},
{name:'渭南市'},
{name:'榆林市'},
{name:'西安市'},
{name:'延安市'},
{name:'咸阳市'},
{name:'安康市'},
{name:'汉中市'},
{name:'铜川市'},
{name:'商洛市'},
]},
{name:'新疆',cityList:[
{name:'阿克苏市'},
{name:'博尔塔拉市'},
{name:'克拉玛依市'},
{name:'昌吉市'},
{name:'哈密市'},
{name:'巴音郭楞市'},
{name:'乌鲁木齐市'},
{name:'五家渠市'},
{name:'石河子市'},
{name:'伊犁市'},
{name:'喀什市'},
]},
{name:'四川',cityList:[
{name:'德阳市'},
{name:'广安市'},
{name:'内江市'},
{name:'攀枝花市'},
{name:'meishan市'},
{name:'乐山市'},
{name:'达州市'},
{name:'凉山市'},
{name:'自贡市'},
{name:'巴中市'},
{name:'遂宁市'},
{name:'泸州市'},
{name:'成都市'},
{name:'绵阳市'},
{name:'雅安市'},
{name:'南充市'},
{name:'资阳市'},
{name:'宜宾市'},
{name:'广元市'},
]},
{name:'江西',cityList:[
{name:'景德镇市'},
{name:'南昌市'},
{name:'鹰潭市'},
{name:'宜春市'},
{name:'抚州市'},
{name:'吉安市'},
{name:'九江市'},
{name:'萍乡市'},
{name:'新余市'},
{name:'上饶市'},
{name:'赣州市'},
]},
{name:'甘肃',cityList:[
{name:'临夏市'},
{name:'定西市'},
{name:'白银市'},
{name:'天水市'},
{name:'武威市'},
{name:'兰州市'},
{name:'酒泉市'},
{name:'平凉市'},
{name:'嘉峪关市'},
{name:'张掖市'},
{name:'陇南市'},
{name:'庆阳市'},
]},
{name:'湖南',cityList:[
{name:'娄底市'},
{name:'益阳市'},
{name:'郴州市'},
{name:'湘西市'},
{name:'长沙市'},
{name:'湘潭市'},
{name:'常德市'},
{name:'邵阳市'},
{name:'张家界市'},
{name:'永州市'},
{name:'株洲市'},
{name:'岳阳市'},
{name:'怀化市'},
{name:'衡阳市'},
]},
{name:'青海',cityList:[
{name:'西宁市'},
]},
{name:'西藏',cityList:[
{name:'拉萨市'},
{name:'林芝市'},
]},
{name:'宁夏',cityList:[
{name:'固原市'},
{name:'银川市'},
{name:'石嘴山市'},
{name:'中卫市'},
{name:'吴忠市'},
]},






{name:'台湾', cityList:[
]},
{name:'香港', cityList:[
]},
{name:'澳门', cityList:[
]}
];