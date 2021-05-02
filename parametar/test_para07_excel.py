#!/usr/bin/env python
# !coding:utf-8

import pytest
import requests
from parameter.para_excel import readExcel
import json


@pytest.mark.parametrize('data', readExcel())
def test_login(data):
    r = requests.post(
        url=data[0],
        json=json.loads(data[1])
    )
    assert r.json()==json.loads(data[2])


if __name__ == '__main__':
    pytest.main(['-s', '-v', "test_para07_excel.py"])
