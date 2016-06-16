# -*- coding: utf-8 -*-
import os,sys

#静态文件打包
def collectstatic():
    os.system('python manage.py collectstatic')
#修改settings
def updateSettings():
    fname = 'conf/settings.py'
    f=open(fname,'r+')
    flist=f.readlines()
    snum = 0
    line = -1
    for fl in flist:
        line += 1
        if 'STATIC_ROOT' in fl: #启用STATIC_ROOT
            if snum==0:
                snum +=1
            else:
                flist[line] = ''
        if 'DEBUG = True' in fl:
            flist[line] = flist[line].replace('DEBUG = True','DEBUG = False')
    f=open(fname,'w+')
    f.writelines(flist)

if __name__ == '__main__':
    if raw_input('yes/no ')=='yes':
        updateSettings()
        collectstatic()