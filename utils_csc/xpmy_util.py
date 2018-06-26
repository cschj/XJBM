# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   Project:     jscrapytask
   IDE Name:    PyCharm
   File Name:   industryXiapiMy
   Email:       hupe_jt@163.com
   Author :     玖天
   Date:        2018/6/5
   Description :虾皮马来西亚行业数据分析
-------------------------------------------------
   Change Activity: 2018/6/5:
-------------------------------------------------
"""
import json

import requests

# from utils import apis, jsonutils
from utils_csc import apis, jsonutils


class ShopeeMy(object):
    def __init__(self):
        pass

    def shopAnalyze(self, shopname):
        '''
        店铺数据获取
        :param shopname:
        :return:
        '''
        response = requests.get(apis.shopeeByshopInfo(shopname))
        shopinfo = json.loads(response.text)
        shopdata = jsonutils.pasce_path('data', shopinfo, is_toStr=False)
        shopmsg = {}
        if shopdata:
            shopmsg['rating_normal'] = jsonutils.pasce_path('rating_normal', shopdata)
            shopmsg['shopid'] = jsonutils.pasce_path('shopid', shopdata)
            shopmsg['rating_bad'] = jsonutils.pasce_path('rating_bad', shopdata)
            shopmsg['mtime'] = jsonutils.pasce_path('mtime', shopdata)
            shopmsg['item_count'] = jsonutils.pasce_path('item_count', shopdata)
            shopmsg['follower_count'] = jsonutils.pasce_path('follower_count', shopdata)
            shopmsg['description'] = jsonutils.pasce_path('description', shopdata)
            shopmsg['rating_good'] = jsonutils.pasce_path('rating_good', shopdata)
            shopmsg['ctime'] = jsonutils.pasce_path('ctime', shopdata)
            shopmsg['name'] = jsonutils.pasce_path('name', shopdata)
            shopmsg['total_avg_star'] = jsonutils.pasce_path('account.total_avg_star', shopdata)
            shopmsg['userid'] = jsonutils.pasce_path('userid', shopdata)
            shopmsg['place'] = jsonutils.pasce_path('place', shopdata)
            shopmsg['last_active_time'] = jsonutils.pasce_path('last_active_time', shopdata)
        return shopmsg

    def shopItemList(self, shopid, pagecount):
        '''
        获取店铺的所有商品信息
        :param shopid:
        :param page:
        :return:
        '''
        iteminfolist = []
        for i in range(0, pagecount):
            url, headers = apis.xpMyShopItemByid(shopid=shopid, page=i)
            response = requests.get(url=url, headers=headers)
            body = response.text
            try:
                if body:
                    shopitems = json.loads(body)
                    items = jsonutils.pasce_path('items', shopitems, is_toStr=False)
                    for next_item in items:
                        itemresult = self.itemInfo(next_item['itemid'], next_item['shopid'])
                        iteminfolist.append(itemresult)
            except Exception as e:
                print(e)
        return iteminfolist

    def itemInfo(self, itemid, shopid):
        '''
        获取商品详情信息
        :param itemid:
        :param shopid:
        :return:
        '''
        try:
            itemapi = apis.xpMyItemInfo(itemid=itemid, shopid=shopid)
            response = requests.get(itemapi)
            body = response.text
            if body:
                iteminfo = json.loads(body)
                itemdata = {}
                item = jsonutils.pasce_path('item', iteminfo, is_toStr=False)
                itemdata['itemid'] = jsonutils.pasce_path('itemid', item, is_toStr=False)
                itemdata['image'] = 'https://cf.shopee.com.my/file/{}'.format(
                    jsonutils.pasce_path('image', item, is_toStr=False))
                itemdata['price_max_before_discount'] = jsonutils.pasce_path('price_max_before_discount', item,
                                                                             is_toStr=False)
                itemdata['shopid'] = jsonutils.pasce_path('shopid', item, is_toStr=False)
                itemdata['price'] = jsonutils.pasce_path('price', item, is_toStr=False)
                itemdata['currency'] = jsonutils.pasce_path('currency', item, is_toStr=False)
                itemdata['raw_discount'] = jsonutils.pasce_path('raw_discount', item, is_toStr=False)
                itemdata['estimated_days'] = jsonutils.pasce_path('estimated_days', item, is_toStr=False)
                itemdata['price_before_discount'] = jsonutils.pasce_path('price_before_discount', item, is_toStr=False)
                itemdata['cmt_count'] = jsonutils.pasce_path('cmt_count', item, is_toStr=False)
                itemdata['catid'] = jsonutils.pasce_path('catid', item, is_toStr=False)
                itemdata['price_min'] = jsonutils.pasce_path('price_min', item, is_toStr=False)
                itemdata['liked_count'] = jsonutils.pasce_path('liked_count', item, is_toStr=False)
                itemdata['status'] = jsonutils.pasce_path('status', item, is_toStr=False)
                itemdata['price_max'] = jsonutils.pasce_path('price_max', item, is_toStr=False)
                itemdata['name'] = jsonutils.pasce_path('name', item, is_toStr=False)
                itemdata['sold'] = jsonutils.pasce_path('sold', item, is_toStr=False)
                itemdata['flag'] = jsonutils.pasce_path('flag', item, is_toStr=False)
                itemdata['url'] = 'https://shopee.com.my/{}-i.{}.{}'.format(itemdata['name'], itemdata['shopid'],
                                                                            itemdata['itemid'])
                return itemdata
        except Exception as e:
            print(e)


if __name__ == '__main__':
    spMy = ShopeeMy()
    shopname = 'yangyangjm.my'
    shopmsg = spMy.shopAnalyze(shopname)

    iteminfolist = spMy.shopItemList(shopmsg['shopid'], 5)
    for itm in iteminfolist:
        print(itm)
