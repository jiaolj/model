# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext#全局模板变量
from tools.func import to_json,getStrTime
from models.news import News
import logging

logger = logging.getLogger("test")

def home(req):
    logger.info('首页 '+getStrTime(1))
    return render_to_response('home.html',locals(),context_instance=RequestContext(req))
