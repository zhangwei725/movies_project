import os
import sys

"""
第一步

在实战开发中,经常讲app规整到一个文件夹下
第一步 在根目录创建apps目录
第二歩 创建的app移动到apps中
第三步  将apps文件设置 source root
第四步 在settings 中加入  sys.path.insert(0,os.path.join(BASE_DIR,'apps'))
注意事项
注册app的时候一定要加上apps目录

第二歩
二级路由配置

第三歩  其他配置
 静态文件的配置
 修改数据配置
 修改语言
 修改时区
"""

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 将apps添加python扫描的路径中
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

SECRET_KEY = 's+!qkiwwiu*7l2jmy%a#0d=cud&6@if5zca9#3l$w-9446!$1i'

DEBUG = True

ALLOWED_HOSTS = []
# 拆分app注册
SYSTEM_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
# 自定义的APP
MY_APPS = [
    'apps.home',
    'apps.account',
]

# 第三方的APP
EXT_APPS = []

INSTALLED_APPS = SYSTEM_APPS + MY_APPS + EXT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_movies.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')]
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_movies.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
"""
sql_mode有三种选项

ANSI 宽松模式  对插入的数据进行校验,如果发现数据长度或者类型不匹配
django框架会对数据类型做跳转.长度的话讲截取(开发中不要使用)
TRADITIONAL 严格模式 能保证数据的准确性,
STRICT_TRANS_TABLES 更严格模式
"""
MYSQL_OPTIONS = {
    'sql_mode': 'TRADITIONAL',
    'charset': 'utf8',
    # 'init_command': 'SET default_storage_engine=INNODB',

}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dj_example',
        'HOST': '112.74.32.121',
        'PORT': '3306',
        'USER':'root',
        'PASSWORD':'root',
        'OPTION': MYSQL_OPTIONS,
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# 修改语言
LANGUAGE_CODE = 'zh-hans'
# 设置中国时区
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
# 是否使用django的时区
USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
#
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'apps/home/static'),
    os.path.join(BASE_DIR, 'apps/account/static'),
)
