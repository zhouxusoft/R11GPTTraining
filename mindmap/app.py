from openai import OpenAI

api_key = "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"

client = OpenAI(api_key=api_key)
desc = input("请输入描述: ")

response = client.chat.completions.create(
    model="gpt-3.5-turbo-1106",
    messages=[
        {
            "role": "system",
            "content": """你是一个软件功能设计助手，你的职责是根据用户提供的软件名称，为该软件设计20个具体的功能模块。每个模块的命名需要直接与软件主要功能相关，以方便单独生成每个功能模块的网页。

最后你需要输出一个JSON对象，它的TypeScript定义为：{list:{name:string,desc:string}[]}，其中list长度为20，name是模块名称，desc是模块介绍""",
        },
        {"role": "user", "content": desc},
    ],
    response_format={"type": "json_object"},
)
content = response.choices[0].message.content
print("-" * 50)
print(content)
