# coding: utf-8
from django.urls import path

from apps.xp_MY.erp_app.views import views_csc

urlpatterns = [

    # #监控中心——店铺监控管理——初始页面
    # path('', monitor_shop_manage_show),
    #
    #
    # # 宝贝近30天每日参加活动
    # path('goods/promotion/<int:bao_id>/', views_li.GoodsPromotion.as_view()),
    
    
    #商品属性查询
    path('vie_search_html/', views_csc.vie_search_html.as_view()),

    #竞争查询 data
    path('vie_search/', views_csc.vie_search.as_view()),

    #test
    path('test/', views_csc.test.as_view()),



]
