"""XP_analysis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from XJBM import views_csc

urlpatterns = [
    path('admin/', admin.site.urls),

    # 首页
    path('', views_csc.index.as_view()),

    path('industry/', include(("apps.xp_MY.industry_analysis_app.urls", "apps.xp_MY.industry_analysis_app"), namespace="industry")),

    path('shop/', include(("apps.xp_MY.shop_analysis_app.urls", "apps.xp_MY.shop_analysis_app"), namespace="shop")),

    path('erp/', include(("apps.xp_MY.erp_app.urls", "apps.xp_MY.erp_app"), namespace="erp")),
]
