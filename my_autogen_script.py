import autogen
import os

config_list = [
    {
        "api_type": "openai",
        "api_key": os.environ.get("OPEN_API_KEY"),
        "model": "gpt-3.5-turbo"
    }
]

assistant = autogen.AssistantAgent(
    name="assistant",
    llm_config={
        "config_list": config_list,
        "seed": 42
    }
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    llm_config={
        "config_list": config_list,
        "seed": 42
    },
    human_input_mode="NEVER"
)

user_proxy.initiate_chat(
    assistant,
    message="What's a fun fact about the universe?"
)

print("Conversation finished.")