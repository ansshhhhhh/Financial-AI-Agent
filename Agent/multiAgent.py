from Agent.agents import web_search_agent, finance_agent, News_agent, Web_agent
from phi.agent import Agent
from phi.model.groq import Groq

agent1 = web_search_agent()
agent2 = finance_agent()
agent3 = News_agent()
agent4 = Web_agent()

def multi_agent():
    return Agent(
        name="Financial Agent",
        role="Use financial agent and News agent to get the information about stock prices and news. Also go through the web to get the information about the company and scrape the web if needed to answer the user's question.",
        model=Groq(id="llama-3.3-70b-versatile"),
        team=[
            agent1,
            agent2,
            agent3,
            agent4
        ],
        instructions=[
            "Always include sources", 
            "Use tables for summary data",
            "Your response should be analytical and should include the information about the company and the stock prices.",
            "If the user's question is about the company, use the web agent to get the information about the company and scrape the web if needed to answer the user's question.",
            "If the user's question is about the stock prices, use the financial agent to get the information about the stock prices and news."
            ],
        show_tools_calls=True,
        add_history_to_messages=True,
        num_history_responses=3,
        markdown=True,
        reasoning= True,
    )