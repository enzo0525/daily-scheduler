from nextcord.ext import commands
from dotenv import load_dotenv
from database import get_discord_id, get_routine_from_day
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import datetime
import nextcord
import os

load_dotenv()
scheduler = AsyncIOScheduler()

intents = nextcord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

def format_text():
    DAYS_OF_WEEK = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = datetime.date.today().weekday() #monday = 0, sunday = 6
    routines = get_routine_from_day(day) #getting data from database depending on day

    if len(routines) == 0:
        return f""">>> # {DAYS_OF_WEEK[day]}
                    ### You're FREE today!
                """

    return f""">>> # {DAYS_OF_WEEK[day]}
                {'\n'.join([f"{index + 1}. {routine['taskName']} - Notes: ({routine['taskNotes']})" for index, routine in enumerate(routines)])}
            """
    
async def send_routine_to_dm():
    user = await bot.fetch_user(get_discord_id())
    if user:
        try:
            message = format_text()
            await user.send(message)
        except Exception as e:
            print(f'ERROR when sending message to user dms: {e}')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    scheduler.start()

scheduler.add_job(send_routine_to_dm, 'cron', hour=0) #Adjust to what time you want to send the message to yourself

bot.run(os.getenv('DISCORD_TOKEN'))