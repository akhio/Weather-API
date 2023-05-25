import discord
from discord.ext import commands
from config import TOKEN, api_key
import aiohttp

# These commands handle the call of BOT in (command_prefix) and including all messages by (discord.Intents.all())
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
client = discord.Client(intents=discord.Intents.all())


# Checking the work of a BOT
@bot.event
async def on_ready():
    print("Bot is ready")


# Main functions
@bot.command()
# Parameters to connect the Weather API
async def weather(ctx: commands.Context, *, city):
    url = "http://api.weatherapi.com/v1/current.json"
    params = {
        "key": api_key,
        "q": city
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            data = await response.json()

            # Data to show up by discord BOT
            location = data["location"]["name"]
            temp = data["current"]["temp_c"]

            # The structure of message
            embed = discord.Embed(title="Weather")
            embed.add_field(name="Temperature", value=f"The temperature in {location} is {temp}C")

            # Sending message
            await ctx.send(embed=embed)

# Running the bot
bot.run(TOKEN)

