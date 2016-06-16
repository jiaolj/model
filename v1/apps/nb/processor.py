# -*- coding: utf-8 -*-
#全局模板变量
def model(request):
    return  {
        'menuList' : [
            {'name':'首页','href':'/','active':'home'},
            {'name':'搜索分析','href':'/analyze/','active':'analyze'},
            {'name':'我的订阅','href':'/custom/','active':'custom'},
        ]
    }