from django.shortcuts import render
from django.views import View

#region 首页

class index(View):
    def get(self,request):

        return render(request,'general/index.html')
#endregion