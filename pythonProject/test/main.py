import requests

# 获取请求数据
def request():
    r = requests.get("http://www.santostang.com/")
    print("文本编码:", r.encoding)
    print("响应状态码:", r.status_code)
    print("响应字符串:", r.text)
    pass

# 地址上的参数编码
def requestParam():
    key_dict = {"key1": "value1", "key2": "value2"}
   # r = requests.get("http://httpbin.org/get", params=key_dict)
    r = requests.post("http://httpbin.org/post", data=key_dict)
    print("编码:", r.url)
    print("文本:", r.text)
    pass


if __name__ == '__main__':
    requestParam()
# request()
