"""
Django settings for dailyfresh project.

Generated by 'django-admin startproject' using Django 1.8.7.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.conf.global_settings import STATICFILES_DIRS, AUTH_USER_MODEL

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p%1lc2v9=7jt-iip%pf2__krb76hpn7ak$u*0f2%p9*lr4ap=p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
AUTH_USER_MODEL = 'users.User'

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.users',  # 用户模块
    'apps.cart',  # 购物车模块
    'apps.orders',  # 订单模块
    'apps.goods',  # 商品模块
    # 'utils',  # 解决模型类继承问题方法一
    'tinymce',  # 使用富文本编辑器
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'dailyfresh.urls'

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

WSGI_APPLICATION = 'dailyfresh.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_dailyfresh',
        'USER': 'root',
        'PASSWORD': 'mysql',
        'HOST': 'localhost',
        'PORT': 3306,
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# 指定静态文件所在的目录
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# 配置富文本编辑器控件显示样式
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',  # 丰富样式
    'width': 600,
    'height': 400,
}

# 邮件发送配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'    # 导入邮件模块
EMAIL_HOST = 'smtp.163.com'                 # 邮箱服务器地址（不同公司的邮箱服务器地址不一样）
EMAIL_PORT = 25                             # 邮箱服务器端口（默认都为25）
EMAIL_HOST_USER = 'chencjhua@163.com'       # 发件人（天天生鲜官方邮箱账号）
EMAIL_HOST_PASSWORD = 'python123'           # 邮箱客户端授权码，非邮箱登录密码
EMAIL_FROM = '天天生鲜<chencjhua@163.com>'   # 收件人接收到邮件后，显示在‘发件人’中的内容，如下图




