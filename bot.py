import discord
from discord.ext import commands, tasks
from noticias import revisar_noticias as obtener_noticias
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


@tasks.loop(minutes=1)
async def revisar_noticias():
    print("Paimon está revisando noticias...")

    canal = discord.utils.get(bot.get_all_channels(), name="𓏼﹒paimon﹒⭐")

    if canal:
        noticia = obtener_noticias()

        if noticia:
            embed = discord.Embed(
                title="🌸 Teyvat News",
                description=f"📰 {noticia['titulo']}\n🔗 {noticia['url']}",
                color=0xf1c40f
            )

            if noticia.get("imagen"):
                embed.set_image(url=noticia["imagen"])

            await canal.send(embed=embed)


@bot.event
async def on_ready():
    revisar_noticias.start()
    print(f"✅ {bot.user} está conectado")


@bot.command()
async def ping(ctx):
    await ctx.send("🏓 ¡Pong! Teyvat News está funcionando.")


bot.run(TOKEN)
