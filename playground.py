from phi.agent import Agent
import phi.api
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo

import os
import openai
from dotenv import load_dotenv
import groq
import phi

from phi.playground import Playground, serve_playground_app
load_dotenv()

phi.api=os.getenv("PHI_API_KEY")

# Hard-code your Groq API key directly for testing purposes
api_key = "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"

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


app = Playground(agents=[finance_agent, web_search_agent]).get_app()

if __name__=="__main__":
    serve_playground_app("playground:app", reload=True)