# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SECRET_KEY = '#)1_b=*kspc$y!freef-8dbc(e!dl_dpi06kx^3f-7gvc(oms('
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []
APP_NAME = 'nb'
INSTALLED_APPS = (
    #'django.contrib.contenttypes',
    'django.contrib.sessions', #会话设置
    #'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.'+APP_NAME,
    'customTags',
    'corsheaders',
    'models',
    'user',
    'tools',
)
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware', #会话设置
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.messages.middleware.MessageMiddleware',
    #'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'user.middleware.QtsAuthenticationMiddleware',
)
#会话设置
#SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE=3600*2
#mysql设置
mysql_ip = '192.168.1.253'
mysql_uname = 'liangzhi'
mysql_passwd = '123456'
#跨域设置
CORS_ORIGIN_ALLOW_ALL = True
CORS_ORIGIN_WHITELIST = (
    'localhost',
)
ROOT_URLCONF = 'conf.urls'
LANGUAGE_CODE = 'zh-cn' 
DEFAULT_CHARSET = 'UTF-8'
WSGI_APPLICATION = 'conf.wsgi.application'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATIC_ROOT = ''
#全局模板变量
TEMPLATE_CONTEXT_PROCESSORS = (
    'customTags.processor.model',
)
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates').replace('\\', '/'),
)
DATABASES = {
   'default': {
         'ENGINE': 'django.db.backends.mysql',
         'NAME': 'model',
         'USER': mysql_uname,
         'PASSWORD': mysql_passwd,
         'HOST': mysql_ip,
         'charset': 'utf8',
   }
}
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static').replace('\\', '/'),
)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',
            'formatter': 'verbose'
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'django_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/django.log',
            'formatter': 'verbose'
        },
        'django_console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'app_file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'logs/'+APP_NAME+'.log',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['django_file', 'django_console'],
            'propagate': True,
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
        'app': {
            'handlers': ['app_file', 'console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'DEBUG'),
        },
    }
}
