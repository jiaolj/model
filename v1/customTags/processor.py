# -*- coding: utf-8 -*-
#全局模板变量
def model(request):
    return  {
        'menuList' : [
            {'name':'歌曲','href':'/success/','active':'music'},
            {'name':'歌手','href':'/project/','active':'singer'},
        ]
    }