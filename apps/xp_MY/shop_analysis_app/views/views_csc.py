import json
import re
import time
import datetime
from urllib import parse

import math
import pymysql
import redis
import requests
from django.db.models import Q, Sum
from django.http import HttpResponse, JsonResponse, request
from django.shortcuts import render, render_to_response
from django.views import View

from lxml import etree



# region 马来西亚

#region 竞争查询初始页面
class vie_search_html(View):
    def get(self,request):
        return render(request, 'shop/table-show.html')
#endregion

#region 竞争查询数据
class vie_search(View):
    def get(self,request):
        print('here')
        result = {'data':[]}
        result = json.dumps(result)
        return HttpResponse(result,content_type="application/json")
#endregion


class test(View):
    def get(self,request):
        result = {'data': []}
        result = json.dumps(result)
        return HttpResponse(result,content_type="application/json")


# endregion



