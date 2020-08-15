import pandas as pd

import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
#c'est le token du bot
GUILD = 'JDR'
#c'est le serveur sur lequel on se trouve (le mien)

bot = commands.Bot(command_prefix='!')
bot.remove_command('help')
@bot.command()
async def help(ctx):
    embed= discord.Embed(title='n.o.x +', description='Un bot de modération doté de cartes de sécurité émotionnelles simples', color = discord.Colour.from_rgb(70, 130, 190))
    
    embed.add_field(name = '!n', value = 'Je ne suis pas à l\'aise avec le sujet, pouvons nous enchaîner ?', inline = False)
    embed.add_field(name = '!o', value = 'Tout va bien pour moi, continuons cette conversation :smile:', inline = False)
    embed.add_field(name = '!x', value = 'J\'aimerais que nous changions de sujet de conversation. Merci.', inline = False)
    embed.add_field(name = '!l', value = 'Pourrions nous revenir sur ce sujet plus tard ? Merci.', inline = False)
    embed.add_field(name = '!m', value = 'Pouvons nous en parler en MP ? Merci.', inline = False)
    embed.add_field(name = '!y', value = 'Pouvez-vous poursuivre votre conversation par MP ? Merci [...].', inline = False)
    embed.add_field(name = '!t', value = 'Attention ! Cette conversation traite d\'un sujet sensible. [...]', inline = False)
    embed.add_field(name = '!c', value = 'Invitez des personnes concerné.e.s à prendre part au débat si iels le souhaitent !.', inline = False)
    embed.add_field(name = '!e', value = 'Cette conversation m\'intéresse mais je dois y aller ! Je reprendrai à partir de là !', inline = False)
   
    await ctx.send(embed=embed)
client = discord.Client()


tab = pd.read_csv('tab_nox.csv', sep = ';', engine = 'python')

# for i in range (0, len(tab)) :
#     if tab.letter[i]== 'x':
#         print('message', tab.img_url[i])
#     elif tab.letter[i]== 'o' :
#         print('message',tab.img_url[i])

command_name = tab.letter

for i in range(0, len(tab)) :
    if tab.letter[i] == 'x':
        txt= tab.txt[i] 
        gif= tab.img_url[i]
        x= txt+gif


        @bot.command(name= tab.letter[i], help = 'a help message')
        async def X_CARD(ctx):

            await ctx.send(x)

    elif tab.letter[i] == 'o':
        txt= tab.txt[i] 
        gif= tab.img_url[i]
        o= txt+gif


        @bot.command(name=tab.letter[i] , help = 'a help message')
        async def O_CARD(ctx):

            await ctx.send(o)
    elif tab.letter[i] == 'n':
        txt= tab.txt[i] 
        gif= tab.img_url[i]
        n= txt+gif


        @bot.command(name=tab.letter[i], help = 'a help message')
        async def N_CARD(ctx):

            await ctx.send(n)

    elif tab.letter[i] == 'l':
        txt= tab.txt[i] 
        gif= tab.img_url[i]
        l= txt+gif


        @bot.command(name=tab.letter[i], help = 'a help message')
        async def L_CARD(ctx):

            await ctx.send(l)

    elif tab.letter[i] == 'm':
        txt= tab.txt[i] 
        gif= tab.img_url[i]
        m= txt+gif


        @bot.command(name=tab.letter[i], help = 'a help message')
        async def M_CARD(ctx):

            await ctx.send(m)

    elif tab.letter[i] == 'y':
        txt= tab.txt[i] 
        gif= tab.img_url[i]
        y= txt+gif


        @bot.command(name=tab.letter[i], help = 'a help message')
        async def Y_CARD(ctx):

            await ctx.send(y)

    elif tab.letter[i] == 't':
        txt= tab.txt[i] 
        gif= tab.img_url[i]
        t= txt+gif


        @bot.command(name=tab.letter[i], help = 'a help message')
        async def T_CARD(ctx):

            await ctx.send(t)

    elif tab.letter[i] == 'c':
        txt= tab.txt[i] 
        gif= tab.img_url[i]
        c = txt+gif


        @bot.command(name=tab.letter[i], help = 'a help message')
        async def C_CARD(ctx):

            await ctx.send(c)

    elif tab.letter[i] == 'e':
        txt= tab.txt[i] 
        gif= tab.img_url[i]
        e= txt+gif


        @bot.command(name=tab.letter[i], help = 'a help message')
        async def E_CARD(ctx):

            await ctx.send(e)


bot.run(TOKEN)