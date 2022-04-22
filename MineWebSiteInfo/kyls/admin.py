from dataclasses import field, fields
from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.models import User
from django.forms import ModelForm


from .models import *


class MyForm(ModelForm):
    class Meta:
        model = Allsite
        fields = "__all__"
        error_messages = {
            "url": {"required": "网址必须非空且唯一"},
            "type": {"required": "类型是必填项 请务必填写!!!"},
            "province": {"required": "省份是必填项 请务必填写!!!"},
            "status": {"required": "状态是必填项 请务必填写!!!"},
        }


@register(Allsite)
class AllsiteAdmin(admin.ModelAdmin):
    list_display = ["id", "is_status", "type", "status", "manager",  "province", "urlname", "url",
                    "classifyps",
                    "remarks", "create_time", "update_time",
                    ]

    # filter  filed
    list_filter = ("type", "status", "manager", "province", "doubletype", "urlname")
    # link  click
    list_display_links = ["id", "province", "urlname", "url", "create_time", "update_time",
                          ]
    # ordering设置默认排序字段，负号表示降序排序
    ordering = ('-id',)
    # 首页可编辑字段
    list_editable = ["status", "manager","remarks", "classifyps", "type", ]
    # 搜索字段
    search_fields = ["id", "type", "status", "manager", "province", "city", "countrytown", "urlname", "url", "urlpath",
                     "classifyps",
                     "remarks", "doubletype"]

    # save_on_top = True

    #
    show_full_result_count = True

    # 最大显示200个
    list_max_show_all = 200

    # 只显示只读字段
    readonly_fields = ("create_time", "update_time",)

    # 每页显示几个
    list_per_page = 10

    # 可以支持 筛选后 不清除筛选
    preserve_filters = True

    # save_on_top = True

    # 保存为新的
    save_as = True
    # 详情业列表显示的字段
    fields = ("type", "status", "manager", "province", "city", "countrytown", "urlname", "url", "urlpath", "classifyps",
              "remarks", "doubletype", "create_time", "update_time",)

    #  首页上 可以进行筛选
    # date_hierarchy = "update_time"


    form = MyForm

    # autocomplete_fields = ()
    # sortable_by = None

    # list_select_related = ["type"]

    def queryset(self,request):
        return super(AllsiteAdmin, self).queryset(request).select_related("id","type", "status", "manager",  "province", "urlname", "url",
                    "classifyps",
                    "remarks", "create_time", "update_time",)

admin.site.site_header = "爬虫管理系统"
admin.site.site_title = "爬虫管理系统"


class MyAdminSite(admin.AdminSite):
    site_header = '爬虫管理系统'  # 此处设置页面显示标题
    site_title = '爬虫系统'  # 此处设置页面头部标题


admin_site = MyAdminSite(name='management')
