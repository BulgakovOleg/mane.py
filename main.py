import discord
import random
from logic import * 
from discord.ext import commands
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True
# Создаем бота в переменной bot и передаем все привелегии
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
@bot.command()
async def commands(ctx):
    await ctx.send("Вот мои команды:$facts - факты о мусоре, $place - место для мусора, $loot - что можно получить с переработки,$helping - помощь с мусором")
@bot.command()
async def facts(ctx):
    await ctx.send(facts_of_trash())
@bot.command()
async def loot(ctx):
    await ctx.send(things_of_trash())
@bot.command()
async def place(ctx):
    await ctx.send(place_for_trash())
@bot.command()
async def helping(ctx):
    await ctx.send(help_with_trash())
