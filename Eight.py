import discord
import logging
import asyncio
import random
from discord.ext.commands import Bot
from discord.utils import find
import EightSpeaks as ES

#logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


eight = Bot(command_prefix="/") #Eightbot

@eight.event
async def on_message(message):
    if message.author == eight.user:
        return #stops him responding to himself
    
    #elif message.content.startswith('o/'):
    #    await eight.send_message(message.channel, '\o') #waves back
    #    await asyncio.sleep(60)
        
    #elif 'o7' in message.content:
    #    await eight.send_message(message.channel, 'o7') #salutes
    #    await asyncio.sleep(60)
    
    #machineLearning
    #ES.learn(message.content)    
    #await eight.send_message(message.channel, ES.speak(message.content))
    
  
@eight.command()
async def hello(*args):
    '''Hello, World'''
    return await eight.say("Hello, world!")

@eight.command()
async def bye(*args):
    '''He says bye'''
    return await eight.say("Goodbye")

@eight.command()
async def fiteme(*args):
    '''Fiteme animation'''
    frames = ["(ง⸌Д⸍)ง","(ง⸌Д⸍)ᓄ","(ᓄ⸌Д⸍)ง","(ง⸌Д⸍)ง","(ᓄ⸌Д⸍)ง","(ง⸌Д⸍)ง"]
    msg = await eight.say(frames[0])
    await asyncio.sleep(.01)
    for x in range(len(frames)-1):
        await eight.edit_message(msg, frames[x+1])
        await asyncio.sleep(.01)
        
@eight.command()
async def dance(*args):
    '''Fance animation'''
    frames =["┏(°.°)┛","┗(°.°)┓","┗(°.°)┛","┏(°.°)┓","┏(°.°)┛","┏( °.°)┛","┏(°.°)┛","┏( °.°)┛","┏(°.°)┛"]
    msg = await eight.say(frames[0])
    await asyncio.sleep(.01)
    for x in range(len(frames)-1):
        await eight.edit_message(msg, frames[x+1])
        await asyncio.sleep(.01)
        
        
        
        
@eight.command()
async def colours(*args):
    '''list of role colours, yes its spelt with a u you imperial bastards'''
    await eight.say("Green, Blue, Violet, Pink, Yellow, Orange, Red")
        
@eight.command(pass_context=True)
async def green(ctx, member: discord.Member = None):
    '''changes role colour'''
    if member is None:
            member = ctx.message.author   
    await eight.replace_roles(member,  find(lambda r: r.name == 'Green', ctx.message.server.roles))
    
@eight.command(pass_context=True)
async def blue(ctx, member: discord.Member = None):
    '''changes role colour'''
    if member is None:
            member = ctx.message.author   
    await eight.replace_roles(member,  find(lambda r: r.name == 'Blue', ctx.message.server.roles))
    
@eight.command(pass_context=True)
async def violet(ctx, member: discord.Member = None):
    '''changes role colour'''
    if member is None:
        member = ctx.message.author   
    await eight.replace_roles(member,  find(lambda r: r.name == 'Violet', ctx.message.server.roles))    
    
@eight.command(pass_context=True)
async def pink(ctx, member: discord.Member = None):
    '''changes role colour'''
    if member is None:
        member = ctx.message.author   
    await eight.replace_roles(member,  find(lambda r: r.name == 'Pink', ctx.message.server.roles))       

@eight.command(pass_context=True)
async def yellow(ctx, member: discord.Member = None):
    '''changes role colour'''
    if member is None:
        member = ctx.message.author   
    await eight.replace_roles(member,  find(lambda r: r.name == 'Yellow', ctx.message.server.roles))    

@eight.command(pass_context=True)
async def orange(ctx, member: discord.Member = None):
    '''changes role colour'''
    if member is None:
        member = ctx.message.author   
    await eight.replace_roles(member,  find(lambda r: r.name == 'Orange', ctx.message.server.roles))    

@eight.command(pass_context=True)
async def red(ctx, member: discord.Member = None):
    '''changes role colour'''
    if member is None:
            member = ctx.message.author   
    await eight.replace_roles(member,  find(lambda r: r.name == 'Red', ctx.message.server.roles))

#ToDo get better insults
"""@eight.command()
async def insult(*args):
    '''insults you like the bitch you are'''
    insultsFile = open('insults.txt', 'r')
    insults = insultsFile.readlines()
    await eight.say(insults[random.randrange(len(insults))])"""

eight.run("MjgxNTQ4MDE0NzM1MDY1MDg5.C4ZjtQ.W73BxNmo9OKq6FIFmC6IsjRvXmE")

