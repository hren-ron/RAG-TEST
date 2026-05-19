

from langchain_community.chat_models.tongyi import ChatTongyi
from langchain.agents import create_agent
from langchain_core.tools import tool

@tool("weather")
def weather(location: str) -> str:
    """查询指定地区的天气信息
    
    Args:
        location: 地区名称，例如：深圳、北京等
        
    Returns:
        str: 天气信息描述
    """
    return "今天深圳的天气是晴天"



agent = create_agent(
    model=ChatTongyi(model="qwen3-max"),
    tools=[weather],
    system_prompt="""
    你是一个智能助手，请回答问题。
    """,
)

res = agent.invoke(
    {
        "messages":[
            {"role":"user", "content":"明天深圳的天气如何"}
        ]
    }
)

for msg in res["messages"]:
    print(type(msg).__name__, msg.content)
