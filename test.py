from Agent.multiAgent import multi_agent
from dotenv import load_dotenv

load_dotenv()

Financial_Agent = multi_agent()

Financial_Agent.print_response("Should i consider Apple stock?", stream=True)
