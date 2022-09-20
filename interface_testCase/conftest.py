import time

import pytest


# 作用范围为类的前后置固件
@pytest.fixture(scope="class")
def gujian_1():
    print("gujian_1前置动作运行一次")
    yield "gujian_1"
    print("gujian_1后置动作运行一次")


# 作用范围为方法的前后置固件
@pytest.fixture(scope="function", autouse="true")
# @pytest.fixture装饰器中，如果传递参数autouse=true，代表此函数会在规定的scope参数范围内自动执行，且不需要在测试方法中进行引用。
def gujian_2():
    print("gujian_2前置动作运行一次")
    yield
    print("gujian_2后置动作运行一次")


# 作用范围为方法的前后置固件
@pytest.fixture(scope="class")
def gujian_3():
    print("gujian_3前置动作运行一次")
    yield "qianzhi_1"
    print("gujian_3后置动作运行一次")
