import requests

# API 地址
url = "http://localhost:11434/api/generate"

# 请求数据
data = {
    "model": "deepseek-r1:1.5b",
    "prompt": "你好，DeepSeek！",
    "stream": False
}

# 发送请求
response = requests.post(url, json=data)

# 解析响应
if response.status_code == 200:
    result = response.json()
    print("模型输出：", result["response"])
else:
    print("请求失败，状态码：", response.status_code)