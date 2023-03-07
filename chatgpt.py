import requests
import json
import time
import color

# 设置OpenAI API的认证密钥和请求参数
url = "https://api.openai.com/v1/chat/completions"

proxie_type = input('是否使用代理：\n0：不使用代理\n其他：输入指定代理,ip:port\n')
if proxie_type == '0':
    proxies = {}
else:
    proxies = {
        "http": f"http://{proxie_type}",
        "https": f"http://{proxie_type}",
    }

api_key = input('请输入api_key：')
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}",
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

# 保存对话历史记录的列表
conversation_history = []
print('按q退出程序')
# 更改回答文本颜色
color_text = color.winColor()

while True:
    # 创建Session对象
    session = requests.Session()

    content = input('请输入问题：')
    if content == 'q' or content == 'Q':
        # 关闭会话
        session.close()
        break
    content_len = len(content)
    # 将用户输入与之前的历史记录一起发送给ChatGPT
    prompt = "\n".join(conversation_history + [content.strip()])
    # print(prompt)
    data = {
        "model": 'gpt-3.5-turbo',
        'messages': [{"role": "user", "content": prompt}],
        'temperature': 0.3,
        'top_p': 1.0,
        'frequency_penalty': 0.0,
        'presence_penalty': 0.0,
        "max_tokens": 2048,
    }
    # 发送请求并获取响应
    response = session.post(url, headers=headers, json=data, proxies=proxies, timeout=None)
    # print(json.loads(response.text))
    msg = json.loads(response.text)["choices"][0]["message"]["content"]
    # 将对话历史记录更新为包括用户输入和生成的响应
    conversation_history.append(content.strip())
    conversation_history.append(msg)
    # print(msg)
    # 以绿色输出回答
    color_text.print_green_text(msg)
    # 等待一段时间再进行下一次迭代，以避免过度使用OpenAI API
    time.sleep(1)
