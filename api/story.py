from flask import Flask, request
import openai
import time
import requests


app = Flask(__name__)

openai.api_key = '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'


@app.route('/get', methods=['GET'])
def get_text():
    text = request.args.get('text', '') 
    text = "I hope you, as a children's story creator, can help me write a Chinese idiom story about '"+text+"', and all the output will be in Chinese"
    return chat_with_gpt3(text)



def chat_with_gpt3(text):
    for i in range(3):  # 最多重试2次，所以总共尝试3次
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": text}
                ]
            )
            return response.choices[0].message.content
        except (openai.error.RequestTimeoutError, requests.exceptions.ProxyError):  # 如果请求超时或者代理错误
            if i < 2:  # 如果还没重试2次
                time.sleep(3)  # 等待1秒后重试
            else:  # 如果已经重试2次
                raise  # 抛出异常

