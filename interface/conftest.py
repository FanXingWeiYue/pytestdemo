import pytest

# 作用范围为方法的前后置固件
@pytest.fixture(scope="class")
def qianzhi_1():
    print("在类执行前要运行一次")
    yield
    print("在类执行后要运行一次")

# 作用范围为方法的前后置固件
@pytest.fixture(scope="function")
def qianzhi_2():
    print("在方法执行前要运行一次")
    yield
    print("在方法执行后要运行一次")