from catbot import CatBot
from echo import EchoBot
from langchain_cat import LangChainCatBot

bot = CatBot()

# Echo bot is a very simple bot that just echoes back the user's last message.
# bot = EchoBot()

# LangChainCatBot is a custom chatbot built on top of ChatGPT and LangChain.
# Add your OpenAI key here, e.g. sk-1234

OPEN_AI_API_KEY = "sk-proj-0O8He3q2UAFlHazfFqyBT3BlbkFJ2yvmMmPA7bnpw6ShKpDj"
bot = LangChainCatBot(OPEN_AI_API_KEY)

from fastapi_poe import run

# Add your Poe API key here. You can go to https://poe.com/create_bot?api=1 to generate one.
POE_API_KEY = "yWqakvXFm39bZBy3VwBFxFhAUa6pRKRv"

run(bot, api_key=POE_API_KEY)