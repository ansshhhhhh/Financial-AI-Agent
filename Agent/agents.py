from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.hackernews import HackerNews
from phi.tools.spider import SpiderTools

model = "llama-3.3-70b-versatile"

# DuckDuckGo Agent
def web_search_agent():
    return Agent(
        name="Web Search Agent",
        role="Search the web for information for financial data.",
        model=Groq(id=model),
        tools=[DuckDuckGo()],
        instructions=[
            "Always include sources",
            "Search the web for information for financial data about the company.",
            ],
        show_tools_calls=True,
        markdown=True
    )

# YFinance Agent
def finance_agent():
    return Agent(
        name="Finance AI Agent",
        role="Provide detailed financial analysis, including stock prices, fundamentals, analyst recommendations, and company news",
        model=Groq(id=model),
        tools=[
            YFinanceTools(
                stock_price=True,
                analyst_recommendations=True,
                company_info=True,
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
        role="Fetch top posts related to finance from Hacker News",
        model=Groq(id=model),
        tools=[HackerNews()],
        instructions=[
            "List headlines and URLs related to finance",
            "Get the top 5 posts related to finance from Hacker News",
            "Get article related company user asked for"
            ],
        show_tools_calls=True,
        markdown=True
    )

# Spider Agent
def Web_agent():
    return Agent(
        name="Spider Agent",
        role="Crawl a target URL and summarize content related to finance",
        model=Groq(id=model),
        tools=[SpiderTools(max_results=5)],
        instructions=[
            "Summarize each page with headings",
            "Go through the links you got from different sources and get finance related information",
            "Get the information about the company from the web and scrape the web if needed to answer the user's question."
            ],
        show_tools_calls=True,
        markdown=True
    )