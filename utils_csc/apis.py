# region 马来西亚


def shopeeByshopInfo(shopname):
    '''
    获取店铺详情信息
    :param shopname:店铺链接后的店铺名称
    :return:
    '''
    shopapi = 'https://shopee.com.my/api/v2/shop/get?username={}'.format(shopname)
    return shopapi


def xpMyItemInfo(itemid, shopid):
    '''
    虾皮马来西亚，获取商品详情数据接口
    :param itemid:
    :param shopid:
    :return:
    '''

    iteminfoaip = 'https://shopee.com.my/api/v2/item/get?itemid={}&shopid={}'.format(itemid, shopid)
    return iteminfoaip


def xpMyShopItemByid(shopid, page):
    '''
    获取店铺的商品id列表
    :param shopid:
    :param page:
    :return:
    '''
    page = page * 20
    ref = "https://shopee.com.my"
    headers = {
        "referer": ref,
        "x-api-source": "pc",
        "x-requested-with": "XMLHttpRequest",
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9'

    }
    itembyapi = 'https://shopee.com.my/api/v1/search_items/?by=sales&match_id={}&limit=20&newest={}&order=desc&page_type=shop'.format(shopid, page)
    return itembyapi, headers


# endregion