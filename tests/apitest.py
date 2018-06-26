import json

import requests
import time

import numpy as np

from tests.apitest2 import Client

shopkey = '4bd4a76fb89c5e08931983ba2947f293ac124c70dca9b5ba7b62f90addb5dbd7'

partner_id = 10898

language = 'en'

category_id = 16

shopid = 25959477


def GetCategories():
    print('GetCategories')

    client = Client()

    body = None

    # 请求方式
    method = 'post'
    # 获取类目api
    uri = 'item/categories/get'

    result = client.execute(uri, method, body)

    result = json.dumps(result)

    print(result)


if __name__ == '__main__':
    GetCategories()