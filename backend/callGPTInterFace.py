import os
from openai import OpenAI

client = OpenAI(
    api_key="sk-73D1Gcc7HW8sIpKUbk4kJ0Ze4wao2hAiJjsMkQ8QoN7AmzBS",
    base_url="https://api.chatanywhere.tech/v1"
)

# 调用GPT3.5-turbo模型进行聊天
def chat_with_gpt(user: str, text: str,max_tokens: int = 100,gpt_model:str='gpt-3.5-turbo') -> str:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": user,
                "content": text,
            }
        ],
        model = gpt_model,
        max_tokens = max_tokens
    )
    answer = chat_completion['choices'][0]['message']['content']
    return answer



