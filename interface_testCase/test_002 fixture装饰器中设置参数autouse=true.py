import requests as requests


class TestLogin:
    def test_aaa(self):  # 该方法虽然传前后置固件，但是qianzhi_2固件设置的autouse=true，所以会自动执行
        res = requests.post(r"http://tcc.taobao.com/cc/json/mobile_tel_segment.htm", data="tel=15727049225")
        print(res.status_code)
