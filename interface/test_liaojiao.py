import pytest
import requests as requests

@pytest.mark.usefixtures("qianzhi_1")#在类声明上面加 @pytest.mark.usefixtures() ，代表这个类里面所有测试用例都会调用该fixture
class TestLogin:
    @pytest.mark.run(order=1)
    def test_liaojiao(self,qianzhi_2):
        res=requests.post(r"http://tcc.taobao.com/cc/json/mobile_tel_segment.htm",data="tel=15727049225")
        print(res.status_code)


