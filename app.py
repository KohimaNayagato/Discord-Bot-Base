# Imports
from datetime import datetime
import json, discord, datetime, logging
from colorama import Fore

# Load json config from file
with open('data/bot/config.json') as f:
    data = json.load(f)
    token = data["TOKEN"]
    prefix = data["PREFIX"]

# Store time and date as a variable (Hour_Minute_Day_Month_Year)
timeinfo = datetime.datetime.now().strftime('%H_%M_%d_%m_%Y')

# Save Discord Intents as variable
intents = discord.Intents.default()
intents.message_content = True

# Define bot user
bot = discord.Client(intents=intents)

# Define log handler as variable
handler = logging.FileHandler(filename='data/logs/data_' + str(timeinfo) + '.log', encoding='utf-8', mode='w')

# Bot startup
@bot.event
async def on_ready():
    print(f'{Fore.MAGENTA}[{Fore.RESET}!{Fore.MAGENTA}]{Fore.RESET} Successfully logged in as {bot.user}') # State in console when bot is initialised


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    if message.content.startswith('test'):
        await message.channel.send('Hello World!') # Placeholders

bot.run(token, log_handler=handler) # Start bot with token and ititialise log handler