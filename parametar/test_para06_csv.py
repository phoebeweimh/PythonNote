import pytest
import requests
from parametar.para_csv   import readcsv
import json

@pytest.mark.parametrize('data',readcsv())
def test_login_csv(data):
    r=requests.post(
        url=data[0],
        json=json.loads(data[1])
    )
    assert r.json()==json.loads(data[2])

if __name__ == '__main__':
    pytest.main(['-s', '-v',"test_para06_csv.py"])
