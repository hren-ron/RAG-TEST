from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 调用模型
completion = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "assistant", "content": "Hi there, how can I help you today?"},
        {"role": "user", "content": "请将下面这段英文翻译成中文：I love programming."}
    ],
    stream=True
)

# 输出结果

for chunk in completion:
    print(
        chunk.choices[0].delta.content,
        end=" ",
        flush=True
      )