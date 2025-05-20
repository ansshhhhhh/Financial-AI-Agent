from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.hackernews import HackerNews
from phi.tools.spider import SpiderTools

model = "llama-3.3-70b-versatile"

# Web Search Agent
def web_search_agent():
    return Agent(
        name="Web Search Agent",
        role="Search the web for information for financial analysis",
        model=Groq(id=model),
        tools=[DuckDuckGo()],
        instructions=["Always include sources"],
        show_tools_calls=True,
        markdown=True
    )

# Finance Agent
def finance_agent():
    return Agent(
        name="Finance AI Agent",
        role="Provide detailed financial analysis, including stock prices, fundamentals, analyst recommendations, and company news",
        model=Groq(id=model),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                stock_fundamentals=True,
                company_news=True
            )
        ],
        instructions=[
            "Always include sources",
            "Use tables for summary data",
            "Generate clear financial insights"
        ],
        show_tools_calls=True,
        markdown=True
    )

# Hacker News Agent
def News_agent():
    return Agent(
        name="HackerNews Agent",
        role="Fetch top posts from Hacker News for financial analysis",
        model=Groq(id=model),
        tools=[HackerNews()],
        instructions=["List headlines and URLs"],
        show_tools_calls=True,
        markdown=True
    )

# Spider Agent
def Web_agent():
    return Agent(
        name="Spider Agent",
        role="Crawl a target URL and summarize content for financial analysis",
        model=Groq(id=model),
        tools=[SpiderTools(max_results=2)],
        instructions=["Summarize each page with headings"],
        show_tools_calls=True,
        markdown=True
    )