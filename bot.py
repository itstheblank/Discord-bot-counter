import discord
from discord.ext import tasks, commands
import datetime
import pytz
import os

TOKEN = 'MTQ3Mzc1NDc4Mzc4MDE4MDA0MQ.G1Tln9.byL-Xns4R-I0GaOzOQ2ny2gAbObuMYp6kdOscg'
CHANNEL_ID = 1453221564161196052
TIMEZONE = pytz.timezone('Asia/Ho_Chi_Minh')
TIME_TO_SEND = datetime.time(hour=2, minute=20, second=0, tzinfo=TIMEZONE)

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

def get_count():
    if not os.path.exists("count.txt"):
        return 1
    with open("count.txt", "r") as f:
        try:
            return int(f.read().strip())
        except ValueError:
            return 1

def update_count(new_count):
    with open("count.txt", "w") as f:
        f.write(str(new_count))

@bot.event
async def on_ready():
    print(f'Bot đã đăng nhập: {bot.user}')
    if not daily_counter.is_running():
        daily_counter.start()

@tasks.loop(time=TIME_TO_SEND)
async def daily_counter():
    channel = bot.get_channel(CHANNEL_ID)
    if channel:
        current_count = get_count()
        
        await channel.send(f"Day {current_count}")
        
        update_count(current_count + 1)
    else:
        print("No channels found!")

bot.run(TOKEN)