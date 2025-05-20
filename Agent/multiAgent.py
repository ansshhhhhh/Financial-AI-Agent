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
        role="Help user with financial analysis",
        model=Groq(id="llama-3.3-70b-versatile"),
        team=[
            agent1,
            agent2,
            agent3,
            agent4
        ],
        instructions=["Always include sources", "Use tables for summary data"],
        show_tools_calls=True,
        add_history_to_messages=True,
        num_history_responses=3,
        markdown=True,
        reasoning= True,
    )