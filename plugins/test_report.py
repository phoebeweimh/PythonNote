import pytest
#参数化parametrize(‘参数，以逗号分隔’，[参数值，可以是列表，元祖，字典，每组数据已逗号分割])

#测试函数
def add(a,b):
    return a+b



#三种参数化的形式，列表，元祖，字典
#参数化列表
@pytest.mark.parametrize('a,b,he',[
    [1,1,2],
    [2,2,4]
])


#pytest测试代码
def test_add(a,b,he):
    assert add(a,b)==he


if __name__ == '__main__':
    pytest.main(['-s','-v',test_report.py])

