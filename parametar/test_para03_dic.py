import pytest
#参数化parametrize(‘参数，以逗号分隔’，[参数值，可以是列表，元祖，字典，每组数据已逗号分割])

#测试函数
def chengfa(e,f):
    return e*f

#三种参数化的形式，列表，元祖，字典
#参数化字典
@pytest.mark.parametrize('data',[
    {'e':5,'f':5,'value':25},
    {'e':6,'f':6,'value':36}
])

def test_chengfa(data):
   assert chengfa(data['e'],data['f'])==data['value']

if __name__ == '__main__':
    pytest.main(['-s','-v',"test_canshuhua.py"])

