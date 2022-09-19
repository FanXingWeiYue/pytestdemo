import requests as requests


class TestLogin:
    def test_aaa(self, qianzhi_1):  # 通过在方法中传参来加前后置固件
        res = requests.post(r"http://tcc.taobao.com/cc/json/mobile_tel_segment.htm", data="tel=15727049225")
        print(res.status_code)
