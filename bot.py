import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
@bot.event
async def on_ready():
    canal = discord.utils.get(bot.get_all_channels(), name="paimon")
    if canal:
        await canal.send("🌸 Teyvat News está conectado correctamente.")
    print(f"✅ {bot.user} está conectado")

bot.run(TOKEN)

