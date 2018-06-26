import time
import json
import hmac, hashlib
from urllib.parse import urljoin
from requests import Request, Session
# from .order import Order
# from .product import Product
# from .variation import Variation
# from .logistic import Logistic
# from .rma import RMA
# from .category import Category

# installed sub-module

# installed_module = {
#     "order": Order,
#     "product": Product,
#     "variation": Variation,
#     "logistic": Logistic,
#     "rma": RMA,
#     "category": Category
# }


# class ClientMeta(type):
#     def __new__(mcs, name, bases, dct):
#         klass = super(ClientMeta, mcs).__new__(mcs, name, bases, dct)
#         setattr(
#             klass, "installed_module",
#             installed_module
#         )
#         return klass

shopkey = '4bd4a76fb89c5e08931983ba2947f293ac124c70dca9b5ba7b62f90addb5dbd7'

partner_id = 10898

language = 'en'

category_id = 62

shopid = 25959477


# class Client(object, metaclass=ClientMeta):
class Client(object):


    # __metaclass__ = ClientMeta
    cached_module = {}
    BASE_URL = "https://partner.shopeemobile.com/api/v1/"
    PER_MINUTE_API_RATE = 1000

    # def __init__(self, shop_id, partner_id, secret_key):
    def __init__(self):


        self.shop_id = shopid
        self.partner_id = partner_id
        self.secret_key = shopkey

    def __getattr__(self, name):
        try:
            value = super(Client, self).__getattribute__(name)
        except AttributeError as e:
            value = self.get_cached_module(name)
            if not value:
                raise e
        return value

    def make_timestamp(self):
        return int(time.time())

    def make_default_parameter(self):
        return {
            "partner_id": self.partner_id,
            "shopid": self.shop_id,
            "timestamp": self.make_timestamp()
        }

    def sign(self, url, body):
        bs = url + "|" + json.dumps(body)
        dig = hmac.new(self.secret_key.encode(), msg=bs.encode(), digestmod=hashlib.sha256).hexdigest()
        return dig

    def build_request(self, uri, method, body):
        method = method.upper()
        url = urljoin(self.BASE_URL, uri)
        authorization = self.sign(url, body)
        headers = {
            "Authorization":authorization
        }
        req = Request(method, url, headers=headers)

        if body:
            if req.method in ["POST", "PUT", "PATH"]:
                req.json = body
            else:
                req.params = body
        return req

    def execute(self, uri, method, body=None):
        parameter = self.make_default_parameter()

        if body is not None:
            parameter.update(body)

        req = self.build_request(uri, method, parameter)
        prepped = req.prepare()
        s = Session()
        resp = s.send(prepped)
        resp = self.build_response(resp)
        return resp

    def build_response(self, resp):

        body = json.loads(resp.text)
        print(body)
        if "error" not in body:
            return body
        else:
            print(AttributeError(body["error"]))
            # raise AttributeError(body["error"])

    def get_cached_module(self, key):
        cached_module = self.cached_module.get(key)

        if not cached_module:
            installed = self.installed_module.get(key)
            if not installed:
                return None
            cached_module = installed(self)
            self.cached_module.setdefault(key, cached_module)
        return cached_module

if __name__ == '__main__':
    pass
    cli = Client()
    # uri = 'item/categories/get'
    uri = 'item/add'

    # uri = 'logistics/channel/get'
    # uri = 'item/attributes/get'

    method = 'post'

    attributes =[]

    logistics = []

    wholesales = []

    wholesale = {'min':1,
                 'max':2,
                 'unit_price':98.0,
                 # 'partner_id':partner_id,
                 # 'shopid':shopid,
                 # 'timestamp':cli.make_timestamp(),
                 }

    logistic1 ={'logistic_id':38011,
               'enabled':True,
               # 'shipping_fee':10.0,
               # 'size_id':12,
               'is_free':False,
               'weight':1.0,
               'package_length':30,
                'package_width':30,
                'package_height':30,
               'days_to_ship':30,
               'wholesales':wholesales}
    logistic2 = {'logistic_id': 38012,
                 'enabled': True,
                 # 'shipping_fee':10.0,
                 # 'size_id':12,
                 'is_free': False,
                 'weight': 1.0,
                 'package_length': 30,
                 'package_width': 30,
                 'package_height': 30,
                 'days_to_ship': 30,
                 'wholesales': wholesales}
    logistic3 = {'logistic_id': 38013,
                 'enabled': False,
                 # 'shipping_fee':10.0,
                 # 'size_id':12,
                 'is_free': False,
                 'weight': 1.0,
                 'package_length': 30,
                 'package_width': 30,
                 'package_height': 30,
                 'days_to_ship': 30,
                 'wholesales': wholesales}
    logistic4 = {'logistic_id': 38014,
                 'enabled': False,
                 # 'shipping_fee':10.0,
                 # 'size_id':12,
                 'is_free': False,
                 'weight': 1.0,
                 'package_length': 30,
                 'package_width': 30,
                 'package_height': 30,
                 'days_to_ship': 30,
                 'wholesales': wholesales}
    logistic5 = {'logistic_id': 38020,
                 'enabled': True,
                 # 'shipping_fee':10.0,
                 # 'size_id':12,
                 'is_free': False,
                 }


    logistics.append(logistic1)
    logistics.append(logistic2)
    logistics.append(logistic3)
    logistics.append(logistic4)
    logistics.append(logistic5)

    attribute1 ={'attributes_id':956,
                'value':'自有品牌',
                }
    attribute2 = {'attributes_id':5054,
                'value':'純棉',
                # 'logistics':logistics,
                  }

    attributes.append(attribute1)
    attributes.append(attribute2)

    image1 = {'url': 'https://img.alicdn.com/bao/uploaded/i3/479184430/TB2.r6FdY1YBuNjSszhXXcUsFXa_!!479184430.jpg_400x400.jpg'}
    image2 = {'url': 'http://wshopee.mdiy.cn/1/14/736/5817/0/c/6/0c6b866e5c4de68064be5c465c57f9e3-dimaiid_text.jpg'}
    # image['attributes'] = attributes

    images = []

    images.append(image1)
    images.append(image2)

    variations =[{
                  'name':'2000夏季新款韓版短袖T恤女士寬鬆大碼半袖上衣時尚學生女裝',
                  'stock':10,
                  'price':99.00,
                  'variation_sku':'件'
                  }]


    body = {
            'category_id':9295,
            'name':'2000夏季新款韓版短袖T恤女士寬鬆大碼半袖上衣時尚學生女裝',
            'description':'字母印花T恤：時尚舒適/精緻不失知性◇個性字母印花圖案，做工精美',
            'price':99.00,
            'stock':10,
            # 'item_sku':'件',
            # 'variations':variations,
            'images': images,
            'attributes':attributes,
            'logistics': logistics,
            'weight': 1.0,
            'package_length': 30,
            'package_width': 30,
            'package_height': 30,
            'days_to_ship': 30,
            # 'wholesales': wholesales,
            'partner_id':partner_id,
            'shopid':shopid,
            'timestamp':cli.make_timestamp()
            }

    # body = {'category_id':9295,
    #         'language':language,
    #         }
    # body = None

    result = cli.execute(uri,method,body)

    result = json.dumps(result)


    print(result)

