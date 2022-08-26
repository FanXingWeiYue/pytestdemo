import json
import yaml


# 读取yaml文件的数据
def read_yaml(yaml_path):
    with open(yaml_path, "r", encoding="utf-8") as f:
        value = yaml.load(f, Loader=yaml.FullLoader)
        return value


# 往yaml文件写入数据
def write_yaml(yaml_path, data):
    with open(yaml_path, "a", encoding="utf-8") as f:
        yaml.dump(data, Loader=yaml.FullLoader)
