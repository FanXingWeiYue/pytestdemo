import pytest
import requests as requests

from common.yamlutil import read_yaml


class TestLogin:
    @pytest.mark.run(order=1)
    def test_aaa(self):  # 该方法虽然没有引用任何
        res = requests.post(r"http://tcc.taobao.com/cc/json/mobile_tel_segment.htm", data="tel=15727049225")
        print(res.status_code)

