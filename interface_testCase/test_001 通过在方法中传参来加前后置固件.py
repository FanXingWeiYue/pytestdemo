import pytest
import requests as requests


class TestLogin:
    def test_aaa(self, qianzhi_1):  # 在方法里面加前置方法，就是把前后置固件方法名传参进来
        res = requests.post(r"http://tcc.taobao.com/cc/json/mobile_tel_segment.htm", data="tel=15727049225")
        print(res.status_code)
