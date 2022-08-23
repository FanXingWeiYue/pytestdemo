import pytest
import requests as requests

from common.yamlutil import read_yaml

@pytest.mark.usefixtures("qianzhi_1")  # 在类声明上面加 @pytest.mark.usefixtures() ，代表这个类里面所有测试用例都会调用该fixture
class TestLogin:
    @pytest.mark.run(order=1)
    def test_aaa(self, qianzhi_2):
        res = requests.post(r"http://tcc.taobao.com/cc/json/mobile_tel_segment.htm", data="tel=15727049225")
        print(res.status_code)

    @pytest.mark.run(order=2)
    def test_bbb(self):
        value = read_yaml("./interface/hh.yaml")
        print(value)
