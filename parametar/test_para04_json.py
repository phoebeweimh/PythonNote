import json

import pytest
import requests
from .paraJs import *

#参数化parametrize(‘参数，以逗号分隔’，[参数值，可以是列表，元祖，字典，每组数据已逗号分割])

# 测试函数
def readjson():
    return json.load(open('loginshuju.json', 'r'))


print(readjson())
