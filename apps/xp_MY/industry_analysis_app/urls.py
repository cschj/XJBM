# coding: utf-8
from django.urls import path

from apps.xp_MY.industry_analysis_app.views import views_csc

urlpatterns = [

    # #监控中心——店铺监控管理——初始页面
    # path('', monitor_shop_manage_show),
    #
    #
    # # 宝贝近30天每日参加活动
    # path('goods/promotion/<int:bao_id>/', views_li.GoodsPromotion.as_view()),
    
    
    #行业首页
    path('whole/', views_csc.industry_whole.as_view()),



]
