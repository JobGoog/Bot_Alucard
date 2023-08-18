# import discord
# from discord.ext import commands
# from config import settings

# intents = discord.Intents.default()
# intents.message_content = True
# bot = commands.Bot(command_prefix='!',intents = intents,)

# @bot.event
# async def on_ready():
#     print('Logged in as {0.user}'.format(bot))

# @bot.event
# async def on_message(message):
#     if message.content.lower() == 'мисикс':
#         await message.channel.send('ты мне нравишься продолжай в том же духе')
#     elif message.content.startswith('!level'):
#         level = int(message.content.split()[1])
#         if level >= 8:
#             role = discord.utils.get(message.guild.roles, name='Хорошист')
#             if role:
#                 await message.author.add_roles(role)
#                 await message.channel.send(f'{message.author.mention} получил роль {role.name}')
#     await bot.process_commands(message)

# bot.run(settings['token']) 