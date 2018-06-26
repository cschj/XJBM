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



#region 行业大盘
class industry_whole(View):
    def get(self,request):

        return render(request,'index.html')
#endregion



