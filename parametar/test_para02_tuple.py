import pytest
#参数化parametrize(‘参数，以逗号分隔’，[参数值，可以是列表，元祖，字典，每组数据已逗号分割])

#测试函数
def jianfa(c,d):
    return c-d

#三种参数化的形式，列表，元祖，字典
#参数化元祖
@pytest.mark.parametrize('c,d,cha',[
    (6,3,3),
    (8,4,4)
])

#pytest测试代码
def test_jianfa(c,d,cha):
    assert jianfa(c,d)==cha


if __name__ == '__main__':
    pytest.main(['-s','-v',test_canshuhua.py])

