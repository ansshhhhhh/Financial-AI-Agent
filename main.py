from Agent.multiAgent import multi_agent
from dotenv import load_dotenv
load_dotenv()

Financial_Agent = multi_agent()

def chat():
    """
    This function is used to chat with the Vitteey Sahaayak.
    """
    print("Vitteey Sahaayak: Hello, I am Vitteey Sahaayak, your financial helper\n\nhow can I help you today? (type '000' to quit)")

    while True:
        user_input = input("\nYou: ")
        if user_input.lower() == "000":
            print("Vitteey Sahaayak: Goodbye!")
            break
        else:
            Financial_Agent.print_response(user_input, stream=True)

if __name__ == "__main__":
    chat()

