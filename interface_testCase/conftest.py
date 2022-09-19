import time

import pytest


# 作用范围为方法的前后置固件
@pytest.fixture(scope="class")
def qianzhi_1():
    print("在类执行前要运行一次")
    yield
    print("在类执行后要运行一次")


# 作用范围为方法的前后置固件
@pytest.fixture(scope="function",autouse="true")
# @pytest.fixture装饰器中，如果传递参数autouse=true，代表此函数会在规定的scope参数范围内自动执行，且不需要在测试方法中进行引用。
def qianzhi_2():
    print("在方法执行前要运行一次")
    yield
    print("在方法执行后要运行一次")
