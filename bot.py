import discord
from discord.ext import commands, tasks
import os
from dotenv import load_dotenv
load_dotenv()
from flask import Flask
from threading import Thread

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot funcionando"

def run():
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))

Thread(target=run).start()

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.guilds = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
@tasks.loop(minutes=5)
async def revisar_noticias():
    canal = discord.utils.get(bot.get_all_channels(), name="𓏼﹒paimon﹒⭐")
    if canal:
        await canal.send("📰 Teyvat News está revisando novedades de Genshin Impact...")
        
@bot.event
async def on_ready():
    revisar_noticias.start()
    canal = discord.utils.get(bot.get_all_channels(), name="𓏼﹒paimon﹒⭐")
    if canal:
        await canal.send("🌸 Teyvat News está conectado correctamente.")
    print(f"✅ {bot.user} está conectado")
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 ¡Pong! Teyvat News está funcionando.")
bot.run(TOKEN)

