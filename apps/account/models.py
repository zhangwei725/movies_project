from django.db import models
from django.contrib.auth.models import AbstractUser

"""
模型开发
1>先定义模型生成表
2>先定义表生成模型 
1> 反向生成模型的时候 inspectdb [表名] >迁移文件的名称 --databases 数据库的名称 
2>inspectdb > models.oy
3>将相应的模型复制到models.py文件中  删除模型下的manager=False
4>生成迁移的文件
5>同步到数据 表已经存在 -migrate --fake-initial命令
"""


class User(AbstractUser):
    phone = models.CharField(max_length=11, unique=True)

    # img = models.ImageField()
    class Meta:
        db_table = 'user'
