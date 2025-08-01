
from discord.ext import commands
import discord
import aiohttp
import ssl
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
reportChannelID: int = 1400330644562776064

# Enable message content intent
intents = discord.Intents.default()
intents.message_content = True

# Create SSL context that doesn't verify certificates (TEMPORARY)
ssl_context = ssl.create_default_context()
ssl_context.check_hostname = False
ssl_context.verify_mode = ssl.CERT_NONE




async def create_bot():
    connector = aiohttp.TCPConnector(ssl=ssl_context)
    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all(), connector=connector)
    
    @bot.event
    async def on_ready():
        channel = bot.get_channel(reportChannelID)
        await channel.send("Fatoom is ready to twerk!")
    
    return bot

# Create and run the bot
import asyncio

async def main():
    bot = await create_bot()
    await bot.start(BOT_TOKEN)

if __name__ == "__main__":
    asyncio.run(main())