import discord
from discord.ext import commands
import os

# Jalankan web server kecil biar Replit gak tidur
from keep_alive import keep_alive
keep_alive()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot online sebagai {bot.user}")

@bot.command()
async def ping(ctx):
    await ctx.send("pong!")

@bot.command()
async def halo(ctx):
    await ctx.send("haii <@{user_id}>")

bot.run(os.getenv('TOKEN'))





