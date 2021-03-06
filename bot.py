import configparser

import discord
from discord.ext import commands

config = configparser.ConfigParser()
config.read("config.ini", encoding='utf-8')

intents = discord.Intents.default()
intents.messages = True

bot = commands.Bot(command_prefix='ap.', help_command=None, intents=intents)


@bot.event
async def on_ready():
    print(f"Bot: {bot.user}")
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(name="за публикациями", type=discord.ActivityType.watching))


@bot.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.TextChannel):
        if message.channel.type == discord.ChannelType.news:
            await message.publish()
            await message.add_reaction("📢")


bot.run(config["Config"]["token"])
