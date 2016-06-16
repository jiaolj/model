# -*- coding: utf-8 -*-
#全局模板变量
def model(request):
    return  {
        'menuList' : [
            {'name':'首页','href':'/','active':'music'},
            {'name':'搜索分析','href':'/success/','active':'music'},
            {'name':'我的订阅','href':'/project/','active':'singer'},
        ]
    }