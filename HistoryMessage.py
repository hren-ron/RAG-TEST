from openai import OpenAI

client = OpenAI(
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
)

# 调用模型
completion = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "system", "content": "你是一个AI助理，回答问题简洁"},
        {"role": "user", "content": "小明有2条宠物狗"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "小红有3条宠物猫"},
        {"role": "assistant", "content": "好的"},
        {"role": "user", "content": "总共有多少条宠物"},
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