from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
import openai
from dotenv import load_dotenv
import groq

load_dotenv()
# Hard-code your Groq API key directly for testing purposes
api_key = ""
groq.api_key = api_key

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama3-70b-8192", api_key=api_key),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tool_calls=True,
    markdown=True,
)


# Financial Data Agent
finance_agent = Agent(
    name= "Finance AI Agent",
    model=Groq(id="llama3-70b-8192", api_key=api_key),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True,company_news=True)],
    instructions=["Use tables to present the data"],
    show_tool_calls=True,
    markdown=True
)



multi_ai_agent = Agent(
    model=Groq(id="llama3-70b-8192", api_key=api_key),
    team=[web_search_agent, finance_agent],
    instructions=["Always include sources", "Use tables to present the data"],
    show_tool_calls=True,
    markdown=True
)



multi_ai_agent.print_response("Summarize analyst recommendations and share latest news on NVDA",stream=True)
