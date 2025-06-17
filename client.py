from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        {
            "math": {
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio"            
            },
            "weather": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http"
            } 
        }
    )

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY environment variable is not set.")
    
    tools = await client.get_tools()
    llm = ChatGroq(model="qwen-qwq-32b", temperature=0.4, api_key=api_key)
    agent = create_react_agent(llm, tools=tools)
    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is (1+8) * 12 / 8?"}]}
    )
    print("Math Response: ", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "What is the weather in Mumbai?"}]}
    )
    print("Weather Response: ", weather_response["messages"][-1].content)

asyncio.run(main())