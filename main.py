import discord
from discord.ext import commands
from config import settings

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=settings['prefix'],intents = intents,)

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!")

    async def on_ready(self):
        print("Bot ready.")


@bot.command(name="hello", help="Say hello")
async def hello(ctx):
    await ctx.channel.send("Hello you!")


# @bot.event
# async def test(messege,ctx):
#     user = ctx.message.author
#     role = discord.utils.get(user.server.roles, name="Test")
#     if messege.author == 'Мистер Мисикс':
#         ansver = discord.Message.content
#         for a in ansver:
#             if a == 8:
#                 await ctx.add_roles(user, role)

#     await ctx.channel.send("Ты мне нравишься, продолжай в том же духе!")



bot.run(settings['token']) 