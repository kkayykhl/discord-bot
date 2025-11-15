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

bot.run(os.getenv('TOKEN'))

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="$", intents=intents)

WELCOME_CHANNEL_ID = 1429414889816399935  # ganti kalau beda
HELPER_ROLE_ID = 1429444341801160795

@bot.event
async def on_ready():
    print(f"{bot.user} is online!")

@bot.event
async def on_member_join(member):
    channel = member.guild.get_channel(1422455029746372734)
    helper_role = member.guild.get_role(1424374430884429905)

    if channel is None:
        print("WELCOME CHANNEL NOT FOUND")
        return

    message = (
        f"Hey {member.mention} welcome to the server.\n"
        f"Cubewerd is a chill place for anyone who just wants to hang out, talk, play games, or mess around with cubes.\n"
        f"You don’t have to be a gamer or a cuber to be here, everyone’s welcome as long as you keep it cool and respectful.\n\n"
        f"Before you start chatting, make sure to read the <#1429415146509434891> things stay comfy for everyone.\n"
        f"We’ve got events, random talks, and a lot of friendly people you can vibe with.\n\n"
        f"Don’t be shy, jump into <#1429419627078750320> and say hi.\n"
        f"Glad to have you here, hope you enjoy your stay and make some good memories in Cubewerd.\n"
        f"tag {helper_role.mention} if u need help"

        @bot.command
        async def joined(ctx):
            await ctx.send(f"Hey {member.mention} welcome to the server.\n"
        f"Cubewerd is a chill place for anyone who just wants to hang out, talk, play games, or mess around with cubes.\n"
        f"You don’t have to be a gamer or a cuber to be here, everyone’s welcome as long as you keep it cool and respectful.\n\n"
        f"Before you start chatting, make sure to read the <#1429415146509434891> things stay comfy for everyone.\n"
        f"We’ve got events, random talks, and a lot of friendly people you can vibe with.\n\n"
        f"Don’t be shy, jump into <#1429419627078750320> and say hi.\n"
        f"Glad to have you here, hope you enjoy your stay and make some good memories in Cubewerd.\n"
        f"tag {helper_role.mention} if u need help")

    )

    await channel.send(message)




