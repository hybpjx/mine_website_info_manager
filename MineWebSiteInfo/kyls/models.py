# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
import datetime
import time

from django.db import models
from django.utils.html import format_html


class Allsite(models.Model):
    STATUS_CHOICES = (
        ("成功", '成功'),
        ("未成功", '未成功'),
        ("未做", '未做'),
        ("网址错误", '网址错误'),
        ("困难网站", '困难网站'),
    )

    TYPE_CHOICES = (
        ("地方政府", "地方政府"),
        ("国家部委", "国家部委"),
        ("拟在建项目", "拟在建项目"),
        ("设备企业", "设备企业"),
        ("矿山企业", "矿山企业"),
        ("设计研究院", "设计研究院"),
        ("新闻媒体", "新闻媒体"),
    )

    MANAGER_CHOICES = (
        ("梁子晨", "梁子晨"),
        ("祁广俊", "祁广俊"),
        ("娄程豪", "娄程豪"),
        ("于婷婷", "于婷婷"),
        ("刘效良", "刘效良"),
        ("赵懿晨", "赵懿晨"),
        ("-", "-"),
    )

    DOUBLE_TYPE_CHOICES = (
        ("通用爬取", "通用爬取"),
        ("不适合单页", "不适合单页"),
        ("单页抓取", "单页抓取"),
        ("困难网站", "困难网站"),
        ("娄程豪", "娄程豪"),
        ("爬虫二期", "爬虫二期"),
        ("祁广俊", "祁广俊"),
        ("四大省", "四大省"),
        ("无网址", "无网址"),
        ("仅首页", '仅首页'),
    )

    id = models.AutoField(db_column='Id', primary_key=True, verbose_name="id", editable=False,
                          auto_created=True)
    type = models.CharField(db_column='Type', max_length=255, verbose_name="类型",
                            choices=TYPE_CHOICES)  # Field name made lowercase.
    province = models.CharField(db_column='Province', max_length=255, verbose_name="省")  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=255, blank=True, null=True,
                            verbose_name="市")  # Field name made lowercase.
    countrytown = models.CharField(db_column='CountryTown', max_length=255, blank=True, null=True,
                                   verbose_name="县")  # Field name made lowercase.
    urlname = models.CharField(db_column='Urlname', max_length=255, blank=True, null=True,
                               verbose_name="网站名")  # Field name made lowercase.
    url = models.TextField(verbose_name="网址", unique=True)
    urlpath = models.CharField(db_column='UrlPath', max_length=255, blank=True, null=True,
                               verbose_name="网站目录")  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=255, verbose_name="状态", choices=STATUS_CHOICES,
                              default="未做")  # Field name made lowercase.
    manager = models.CharField(db_column='Manager', max_length=255, blank=True, null=True, verbose_name="管理员",
                               choices=MANAGER_CHOICES)  # Field name made lowercase.
    classifyps = models.CharField(db_column='ClassifyPs', max_length=255, blank=True, null=True,
                                  verbose_name="liuxl")  # Field name made lowercase.
    remarks = models.CharField(max_length=255, blank=True, null=True, verbose_name="备注")
    doubletype = models.CharField(db_column='DoubleType', max_length=255, blank=True, null=True, verbose_name="二次类别筛选",
                                  choices=DOUBLE_TYPE_CHOICES)  # Field name made lowercase.
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")

    class Meta:
        managed = False
        db_table = 'AllSite'
        verbose_name = "目标网站"
        verbose_name_plural = "目标网站"

    # 成功", '成功'),
    #         ("未成功", '未成功'),
    #         ("未做", '未做'),
    #         ("无网址", '无网址'),
    #         ("网址错误", '网址错误'),
    #         ("其他", '其他'),
    def is_status(self):
        if self.status == '成功':
            format_td = format_html('<span style="padding:2px;background-color:green;color:white">成功</span>')
        elif self.status == '网址错误':
            format_td = format_html('<span style="padding:2px;background-color:yellow;color:black">网址错误</span>')
        elif self.status == '未成功':
            format_td = format_html('<span style="padding:2px;background-color:red;color:white">未成功</span>')
        elif self.status == '困难网站':
            format_td = format_html('<span style="padding:2px;background-color:brown;color:white">困难</span>')
        elif self.status == '未做':
            format_td = format_html('<span style="padding:2px;background-color:white;color:black">未做</span>')
        else:
            format_td = format_html('<span style="padding:2px;background-color:black;color:white">???</span>')
        return format_td

    is_status.short_description = "当前状态"

    # def now_time(self):
    #     NowData = int(time.time())
    #     update_time = int(time.mktime(self.update_time))
    #     if str(update_time) <= str(NowData):
    #         ret = "今日已修改"
    #         color = "green"
    #         return format_html('<span style="color:{};">{}</span>', color, ret, )
    #     else:
    #         ret = "今日未修改"
    #         color = "red"
    #         return format_html('<span style="color:{};">{}</span>', color, ret, )
    #
    # now_time.short_description = "时间标记"