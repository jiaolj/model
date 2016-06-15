# -*- coding: utf-8 -*-
from tools.func import to_json,getStrTime
from models.user import User
import logging

logger = logging.getLogger("test")
def loggerInfo(msg):
    logger.info(msg+' '+getStrTime(1))

def get(req):
    back = {'state':'ok'}
    back['data'] = req.session.get('user_token')
    if back['data']:
        back['msg'] = 'get user_token ok'
    else:
        back['state'] = 'error'
        back['msg'] = 'expire or logout'
    return to_json(back)

def login(req):
    back = {'state':'ok'}
    q = req.GET or req.POST
    uname = q.get('uname')
    passwd = q.get('passwd')
    if uname and passwd:
        r = User.objects.filter(uname=uname,passwd=passwd)
        if r:
            req.session['user_token'] = {'uname':uname,'rank':r[0].rank}
            back['msg'] = 'login ok'
            loggerInfo('uname:'+uname+', '+back['msg'])
        else:
            back['state'] = 'error'
            back['msg'] = 'uname or passwd error'
            loggerInfo('uname:'+uname+' passwd:'+passwd+', login error:'+back['msg'])
    else:
        back['state'] = 'error'
        back['msg'] = 'need uname or passwd'
        loggerInfo('login error:'+back['msg'])
    return to_json(back)

def logout(req):
    back = {'state':'ok'}
    if req.session.get('user_token'):
        uname = req.session['user_token']['uname']
        del req.session['user_token']
        back['msg'] = 'logout'
        loggerInfo('uname:'+uname+', '+back['msg'])
    else:
        back['msg'] = 'already logout'
    return to_json(back)