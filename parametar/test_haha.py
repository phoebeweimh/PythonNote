# test_demo1.py
import pytest
import requests
def test_1():
    assert 1+1 >= 2

def test_2():
    res = requests.get('https:www.baidu.com')
    assert res.status_code == 200

if __name__ == '__main__':
    pytest.main(['-s', '-v',"test_haha.py"])