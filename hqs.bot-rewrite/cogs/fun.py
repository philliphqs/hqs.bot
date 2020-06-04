# ----------------------------------------------#
# hqs.bot ©                                     #
# by phillip.hqs ∫ Thanks to alphaSnosh         #
# ----------------------------------------------#

import asyncio
import random

import discord
import lyricsgenius
# import tenorpy
import tweepy
from discord.ext import commands

import botsetup

# colors
blue = 0x0062ff
black = 0x000000
yellow = 0xf5ff30
white = 0xffffff
green = 0x21ff55
grey = 0x636363
darkgrey = 0x1c1c1c
red = 0xff2121
purple = 0xb338ff
pink = 0xff47e0
lightblue = 0x4778ff
lightgreen = 0x73ffad
orange = 0xff9757



# dont edit
consumer_key = botsetup.consumer_key
consumer_secret = botsetup.consumer_secret
access_token = botsetup.access_token
access_token_secret = botsetup.access_token_secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# quotes
quote_1 = botsetup.quote_1
quote_2 = botsetup.quote_2
quote_3 = botsetup.quote_3
quote_4 = botsetup.quote_4
quote_5 = botsetup.quote_5
quote_6 = botsetup.quote_6
quote_7 = botsetup.quote_7
quote_8 = botsetup.quote_8
quote_9 = botsetup.quote_9
quote_10 = botsetup.quote_10

# dice emoji
dice_1 = botsetup.dice_1
dice_2 = botsetup.dice_2
dice_3 = botsetup.dice_3
dice_4 = botsetup.dice_4
dice_5 = botsetup.dice_5
dice_6 = botsetup.dice_6

watermark = 'hqs.bot / by phillip.hqs'

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def battle(self, ctx, tc1: discord.Member, tc2: discord.Member):
        try:
            user = [tc1, tc2]
            hitu1 = f'{tc1} choose a card!'
            hitu2 = f'{tc2} choose a card!'
            rndmc = ['https://i.pinimg.com/originals/9b/bb/70/9bbb7015af1bcd420ee07d89048cebf7.jpg',
                     'https://pics.me.me/thumb_earth-angry-german-kid-spellcastor-tuner-he-rages-about-lag-and-52634494.png',
                     'https://www.memesmonkey.com/images/memesmonkey/cb/cbc69b7a454ec9f50fa0616ca3d4d4d9.jpeg',
                     'https://i.imgur.com/gq8aDzq.jpg',
                     'https://i.redd.it/gqse7u1cudw31.png',
                     'https://i.imgur.com/yeD5fGI.gif',
                     'https://images-na.ssl-images-amazon.com/images/I/51jxIccbroL._AC_.jpg',
                     'https://images-cdn.9gag.com/photo/aDzZ1LO_460s.jpg']

            fight = discord.Embed(title=f'{tc1} \n'
                                        f'VS. \n'
                                        f'{tc2}\n', description='FIGHT!!!')
            fight.set_thumbnail(url='https://media3.giphy.com/media/dw5SDFsmqFhYs/giphy.gif')
            fight.set_footer(text=watermark)
            fight1 = await ctx.send(embed=fight)

            hit = discord.Embed(title=hitu2, color=botsetup.error)
            hit.set_image(url=random.choice(rndmc))
            hit_ = await ctx.send(embed=hit)
            await asyncio.sleep(7)

            hit2 = discord.Embed(title=hitu1, color=blue)
            hit2.set_image(url=random.choice(rndmc))
            hit2_ = await ctx.send(embed=hit2)
            await asyncio.sleep(7)

            hit3 = discord.Embed(title=hitu2, color=botsetup.error)
            hit3.set_image(url=random.choice(rndmc))
            hit3_ = await ctx.send(embed=hit3)
            await asyncio.sleep(7)

            hit4 = discord.Embed(title=hitu1, color=blue)
            hit4.set_image(url=random.choice(rndmc))
            hit4_ = await ctx.send(embed=hit4)
            await asyncio.sleep(7)

            hit5 = discord.Embed(title=hitu2, color=botsetup.error)
            hit5.set_image(url=random.choice(rndmc))
            hit5_ = await ctx.send(embed=hit5)
            await asyncio.sleep(7)

            hit6 = discord.Embed(title=hitu1, color=blue)
            hit6.set_image(url=random.choice(rndmc))
            hit6_ = await ctx.send(embed=hit6)
            await asyncio.sleep(7)

            await fight1.delete()
            await hit_.delete()
            await hit2_.delete()
            await hit3_.delete()
            await hit4_.delete()
            await hit5_.delete()
            await hit6_.delete()
            winner = discord.Embed(title=f'{random.choice(user)} WINS!!!\n', description=f'{tc1}\n'
                                                                                         f' VS. '
                                                                                         f'{tc2}'
                                                                                         f'explore more commands with /help',
                                   color=botsetup.error)
            winner.set_thumbnail(
                url='https://steamuserimages-a.akamaihd.net/ugc/94979365059772671/2FE7825E5D949994966270D1AA6CE4A55DD6773E/')
            winner.set_footer(text="hqs.bot ∫ by phillip.hqs")
            await ctx.send(embed=winner)
        except:
            error = discord.Embed(title='Cant find any user', description='User ```<@user>``')
            await ctx.send(embed=error)

    @battle.error
    async def battle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=botsetup.nouser)

    @commands.command()
    async def pokemonbattle(self, ctx, tc1: discord.Member, tc2: discord.Member):
        try:
            user = [tc1, tc2]
            hitu1 = f'{tc1} choose a card!'
            hitu2 = f'{tc2} choose a card!'
            rndmc = ['https://www.gate-to-the-games.de/images/product_images/popup_images/Teams-sind-Trumpf-30.jpg',
                     'https://webimg.secondhandapp.com/w-i-mgl/5d5f064919d3424f7781f90f',
                     'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcRYP5DtvWuYvI5CjaoaQXJQTn3vJNkOhpg4oUc1qMx3InN2bAld&usqp=CAU',
                     'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSfZXsBQwuPTJOLlabukHgHm5oZOAbjwPRYJQ2evEsmJ01stU5s&usqp=CAU',
                     'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcSOOgRc0Dw46bHdRhSikbxC6a_eWyaPjaKrPu0WaW18zpfJx6Oo&usqp=CAU',
                     'https://assets.pokemon.com/assets/cms2-de-de/img/cards/web/SM8/SM8_DE_201.png',
                     'https://www.pokewiki.de/images/3/31/Lugia-LEGENDE_%28HeartGold_%26_SoulSilver_113%29.jpg',
                     'https://cardsandcars.de/media/image/19/ef/8c/shop-Pokemon_NACHTiFlammen_DE_067_147_600x600.jpg']

            fight = discord.Embed(title=f'{tc1} '
                                        f' VS. '
                                        f'{tc2}', description='FIGHT!!!')
            fight.set_thumbnail(url='https://media3.giphy.com/media/dw5SDFsmqFhYs/giphy.gif')
            fight.set_footer(text="hqs.bot ∫ by phillip.hqs")
            fight1 = await ctx.send(embed=fight)

            hit = discord.Embed(title=hitu2, color=botsetup.error)
            hit.set_image(url=random.choice(rndmc))
            hit_ = await ctx.send(embed=hit)
            await asyncio.sleep(7)

            hit2 = discord.Embed(title=hitu1, color=blue)
            hit2.set_image(url=random.choice(rndmc))
            hit2_ = await ctx.send(embed=hit2)
            await asyncio.sleep(7)

            hit3 = discord.Embed(title=hitu2, color=botsetup.error)
            hit3.set_image(url=random.choice(rndmc))
            hit3_ = await ctx.send(embed=hit3)
            await asyncio.sleep(7)

            hit4 = discord.Embed(title=hitu1, color=blue)
            hit4.set_image(url=random.choice(rndmc))
            hit4_ = await ctx.send(embed=hit4)
            await asyncio.sleep(7)

            hit5 = discord.Embed(title=hitu2, color=botsetup.error)
            hit5.set_image(url=random.choice(rndmc))
            hit5_ = await ctx.send(embed=hit5)
            await asyncio.sleep(7)

            hit6 = discord.Embed(title=hitu1, color=blue)
            hit6.set_image(url=random.choice(rndmc))
            hit6_ = await ctx.send(embed=hit6)
            await asyncio.sleep(7)

            await fight1.delete()
            await hit_.delete()
            await hit2_.delete()
            await hit3_.delete()
            await hit4_.delete()
            await hit5_.delete()
            await hit6_.delete()
            winner = discord.Embed(title=f'{random.choice(user)} WINS!!!\n', description=f'{tc1}'
                                                                                         f' VS. '
                                                                                         f'{tc2}'
                                                                                         f'explore more commands with /help',
                                   color=botsetup.error)
            winner.set_thumbnail(
                url='https://cdna.artstation.com/p/assets/images/images/015/814/178/original/jean-baptiste-gabert-pokemonmockup.gif?1549763590')
            winner.set_footer(text=watermark)
            await ctx.send(embed=winner)
        except:
            error = discord.Embed(title='Cant find any user', description='User ```<@user>``')
            await ctx.send(embed=error)

    @pokemonbattle.error
    async def pokemonbattle_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=botsetup.nouser)

    @commands.command()
    async def tournament(self, ctx, tc1: discord.Member, tc2: discord.Member, tc3: discord.Member, tc4: discord.Member):
        try:
            user = [tc1, tc2, tc3, tc4]
            hitu1 = f'{tc1} choose a card!'
            hitu2 = f'{tc2} choose a card!'
            hitu3 = f'{tc3} choose a card!'
            hitu4 = f'{tc4} choose a card!'
            rndmc = ['https://i.pinimg.com/originals/9b/bb/70/9bbb7015af1bcd420ee07d89048cebf7.jpg',
                     'https://pics.me.me/thumb_earth-angry-german-kid-spellcastor-tuner-he-rages-about-lag-and-52634494.png',
                     'https://www.memesmonkey.com/images/memesmonkey/cb/cbc69b7a454ec9f50fa0616ca3d4d4d9.jpeg',
                     'https://i.imgur.com/gq8aDzq.jpg',
                     'https://i.redd.it/gqse7u1cudw31.png',
                     'https://i.imgur.com/yeD5fGI.gif',
                     'https://images-na.ssl-images-amazon.com/images/I/51jxIccbroL._AC_.jpg',
                     'https://images-cdn.9gag.com/photo/aDzZ1LO_460s.jpg']

            fight = discord.Embed(title=f'{tc1} '
                                        f' VS. '
                                        f'{tc2}', description='FIGHT!!!')
            fight.set_thumbnail(url='https://media3.giphy.com/media/dw5SDFsmqFhYs/giphy.gif')
            fight.set_footer(text="hqs.bot ∫ by phillip.hqs")
            fight1 = await ctx.send(embed=fight)

            hit = discord.Embed(title=hitu1, color=botsetup.error)
            hit.set_image(url=random.choice(rndmc))
            hit_ = await ctx.send(embed=hit)
            await asyncio.sleep(7)

            hit2 = discord.Embed(title=hitu2, color=blue)
            hit2.set_image(url=random.choice(rndmc))
            hit2_ = await ctx.send(embed=hit2)
            await asyncio.sleep(7)

            hit3 = discord.Embed(title=hitu3, color=orange)
            hit3.set_image(url=random.choice(rndmc))
            hit3_ = await ctx.send(embed=hit3)
            await asyncio.sleep(7)

            hit4 = discord.Embed(title=hitu4, color=green)
            hit4.set_image(url=random.choice(rndmc))
            hit4_ = await ctx.send(embed=hit4)
            await asyncio.sleep(7)

            hit5 = discord.Embed(title=hitu1, color=botsetup.error)
            hit5.set_image(url=random.choice(rndmc))
            hit5_ = await ctx.send(embed=hit5)
            await asyncio.sleep(7)

            hit6 = discord.Embed(title=hitu2, color=blue)
            hit6.set_image(url=random.choice(rndmc))
            hit6_ = await ctx.send(embed=hit6)
            await asyncio.sleep(7)

            hit7 = discord.Embed(title=hitu3, color=orange)
            hit7.set_image(url=random.choice(rndmc))
            hit7_ = await ctx.send(embed=hit7)
            await asyncio.sleep(7)

            hit8 = discord.Embed(title=hitu4, color=green)
            hit8.set_image(url=random.choice(rndmc))
            hit8_ = await ctx.send(embed=hit8)
            await asyncio.sleep(7)

            hit9 = discord.Embed(title=hitu2, color=botsetup.error)
            hit9.set_image(url=random.choice(rndmc))
            hit9_ = await ctx.send(embed=hit9)
            await asyncio.sleep(7)

            hit10 = discord.Embed(title=hitu1, color=blue)
            hit10.set_image(url=random.choice(rndmc))
            hit10_ = await ctx.send(embed=hit10)
            await asyncio.sleep(7)

            hit11 = discord.Embed(title=hitu2, color=botsetup.error)
            hit11.set_image(url=random.choice(rndmc))
            hit11_ = await ctx.send(embed=hit11)
            await asyncio.sleep(7)

            hit12 = discord.Embed(title=hitu1, color=blue)
            hit12.set_image(url=random.choice(rndmc))
            hit12_ = await ctx.send(embed=hit12)
            await asyncio.sleep(7)

            await fight1.delete()
            await hit_.delete()
            await hit2_.delete()
            await hit3_.delete()
            await hit4_.delete()
            await hit5_.delete()
            await hit6_.delete()
            await hit7_.delete()
            await hit8_.delete()
            await hit9_.delete()
            await hit10_.delete()
            await hit12_.delete()
            winner = discord.Embed(title=f'{random.choice(user)} WINS!!!\n', description=f'{tc1}'
                                                                                         f' VS. '
                                                                                         f'{tc2}'
                                                                                         f'explore more commands with /help',
                                   color=botsetup.error)
            winner.set_thumbnail(
                url='https://cdna.artstation.com/p/assets/images/images/015/814/178/original/jean-baptiste-gabert-pokemonmockup.gif?1549763590')
            winner.set_footer(text=watermark)
            await ctx.send(embed=winner)
        except:
            error = discord.Embed(title='Cant find any user', description='User ```<@user>``')
            await ctx.send(embed=error)

    @tournament.error
    async def tournament_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=botsetup.nouser)

    @commands.command(pass_context=True)
    async def coinflip(self, ctx):
        flip = random.choice([
            f'https://upload.wikimedia.org/wikipedia/de/thumb/8/80/2_euro_coin_Eu_serie_1.png/220px-2_euro_coin_Eu_serie_1.png',
            f'https://www.zwei-euro.com/wp-content/uploads/2019/02/DE-2002.gif'])
        flipcoin = discord.Embed()
        flipcoin.colour = 0x12423
        flipcoin.set_thumbnail(
            url="https://media1.tenor.com/images/938e1fc4fcf2e136855fd0e83b1e8a5f/tenor.gif?itemid=5017733")
        flipcoin1 = await ctx.send(embed=flipcoin)
        coin = discord.Embed()
        coin.set_thumbnail(url=f'{flip}')
        await asyncio.sleep(2)
        await flipcoin1.delete()
        await ctx.send(embed=coin)

    @commands.command()
    async def minesweeper(self, ctx):
        field00 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field01 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field02 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field03 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field04 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field05 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field06 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field07 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field08 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])

        field10 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field11 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field12 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field13 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field14 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field15 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field16 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field17 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field18 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])

        field20 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field21 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field22 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field23 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field24 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field25 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field26 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field27 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field28 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])

        field30 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field31 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field32 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field33 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field34 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field35 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field36 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field37 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field38 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])

        field40 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field41 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field42 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field43 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field44 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field45 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field46 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field47 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field48 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])

        field50 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field51 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field52 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field53 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field54 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field55 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field56 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field57 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field58 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])

        field60 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field61 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field62 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field63 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field64 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field65 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field66 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field67 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field68 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])

        field70 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field71 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field72 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field73 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field74 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field75 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field76 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field77 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field78 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])

        field80 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field81 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field82 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field83 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field84 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field85 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field86 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field87 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])
        field88 = random.choice(['1️⃣', '2️⃣', '3️⃣', '💥'])

        minesweeper = f"""
            || {field00} || || {field10} || || {field20} || || {field30} || || {field40} || || {field50} || || {field60} || || {field70} || || {field80} ||
            || {field01} || || {field11} || || {field21} || || {field31} || || {field41} || || {field51} || || {field61} || || {field71} || || {field81} ||
            || {field02} || || {field12} || || {field22} || || {field32} || || {field42} || || {field52} || || {field62} || || {field72} || || {field82} ||
            || {field03} || || {field13} || || {field23} || || {field33} || || {field43} || || {field53} || || {field63} || || {field73} || || {field83} ||
            || {field04} || || {field14} || || {field24} || || {field34} || || {field44} || || {field54} || || {field64} || || {field74} || || {field84} ||
            || {field05} || || {field15} || || {field25} || || {field35} || || {field45} || || {field55} || || {field65} || || {field75} || || {field85} ||
            || {field06} || || {field16} || || {field26} || || {field36} || || {field46} || || {field56} || || {field66} || || {field76} || || {field86} ||
            || {field07} || || {field17} || || {field27} || || {field37} || || {field47} || || {field57} || || {field67} || || {field77} || || {field87} ||
            || {field08} || || {field18} || || {field28} || || {field38} || || {field48} || || {field58} || || {field68} || || {field78} || || {field88} ||
            """
        await ctx.send(f'{minesweeper}')

    @commands.command()
    async def rolldice(self, ctx):
        dice = [f'{dice_1}',
                f'{dice_2}',
                f'{dice_3}',
                f'{dice_4}',
                f'{dice_5}',
                f'{dice_6}']
        rolldice = discord.Embed(title=f'You have rolled {random.choice(dice)}',
                                 description=f'write {botsetup.prefix}help to explore more commands',
                                 color=lightblue)
        rolldice.set_footer(text="hqs.bot ∫ by phillip.hqs")
        await ctx.send(embed=rolldice)

    @commands.command()
    async def tweet(self, ctx, *, args):
        await ctx.send(embed=botsetup.nota)
        #if args:
        #    with open("blacklist_words.txt") as file:
        #        bad_words = [bad_word.strip().lower() for bad_word in file.readlines()]
        #        message_content = args
        #        for bad_word in bad_words:
        #            if bad_word in message_content:
        #                blacklist = discord.Embed(title='Dont insult or advertise',
        #                                          description='check [rules](https://hqs.bplaced.net/rules.html)',
        #                                          color=red)
        #                await ctx.send(embed=blacklist)
        #                return
        #    try:
        #        api.update_status(status=f"New Tweet from the alphaclan server\n"
        #                                 f"---------------\n"
        #                                 f"tweet author: {ctx.author}\n"
        #                                 f"{args}\n"
        #                                 f"---------------\n"
        #                                 f'check out!\n'
        #                                 f"alphaclan: https://discord.gg/uFdVUMH\n"
        #                                 f"website: https://hqs.sytes.net\n")
        #        tweet1 = discord.Embed(title=f'Your tweet was sent successfully 😃',
        #                               description=f'[Click here](https://twitter.com/alphaclanc) to see your tweet on tweet on twitter\n'
        #                                           f'```{args}```', color=lightblue)
        #        tweet1.set_footer(text="hqs.bot ∫ by phillip.hqs")
        #        await ctx.send(embed=tweet1)
        #    except:
        #        tweetfailed = discord.Embed(title='Check your Tweet!', description=f'`{args}`')
        #        tweetfailed.set_footer(text=watermark)
        #        await ctx.send(embed=tweetfailed)

    @commands.command()
    async def quote(self, ctx):
        quotes = [quote_1,
                  quote_2,
                  quote_3,
                  quote_4,
                  quote_5,
                  quote_6,
                  quote_7,
                  quote_8,
                  quote_9,
                  quote_10]
        quote = discord.Embed(title='Quote:', description=f'{random.choice(quotes)}', color=green)
        quote.set_footer(text=watermark)
        await ctx.send(embed=quote)

    @commands.command()
    async def genius(self, ctx, *, arg1):
        import json
        import requests
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"

        try:
            loadingly = discord.Embed(title=f'Song/Artist: {arg1}', description='This can take few minutes',
                                      color=0xfffca1)
            loadingly.set_footer(text="hqs.bot ∫ by phillip.hqs")
            loadingly.set_author(name="Search Songtext",
                                 icon_url="https://www.koester-planung.de/_Resources/Static/Packages/Avency.KoesterBau.Base/Images/ajax-loader.gif")
            genius = lyricsgenius.Genius("A27ABe0jwhSJ_I1AJKNZOGBKzLjFHDeHFz1fMnNgbMo87PAE9y4UR_t9vZDuj6qe")
            loadingly
            song = genius.search_song(f"{arg1}")
            loadingly1 = await ctx.send(embed=loadingly)
            loadingly = discord.Embed(title='Loading Song...', description='This can take few minutes')
            loadingly.set_footer(text="hqs.bot ∫ by phillip.hqs")
            # try:
            querystring = {"q": f"{song.title} {song.artist}"}
            headers = {
                'x-rapidapi-host': botsetup.rapidapihost, 
                'x-rapidapi-key': botsetup.rapidapikey
            }
            response = requests.request("GET", url, headers=headers, params=querystring)
            x = response.text
            y = json.loads(x)
            title = y["data"][0]["title"]
            min = y["data"][0]["duration"]
            preview = y["data"][0]["preview"]
            lyric = discord.Embed(title=f'Song: {song.title}', description=f'Duration: {min} minutes\n'
                                                     f'Preview: [Play now]({preview})\n'
                                                                           f' \n'
                                                                           f'{song.lyrics}\n'
                                                                           f'  \n'
                                                                           f'Song by {song.artist}\n',
                                  color=botsetup.geniusc)

            lyric.set_footer(text="hqs.bot ∫ by phillip.hqs")
            lyric.set_author(name="Genius",
                             icon_url="https://apkdirectory.com/logos/genius-song-lyrics-038-more.png", )
            await asyncio.sleep(5)
            await loadingly1.delete()
            try:
                await ctx.send(embed=lyric)
            except:
                file1 = open(f'genius_lyric.txt', 'w')
                file1.write('hqs.bot / by phillip.hqs\n'
                            '      \n')
                file1.write(song.lyrics)
                file1.write('      \n'
                            'hqs.bot / by phillip.hqs')
                file1.close()
                finishdl = discord.Embed(title="You can download the lyric from the song:",
                                         description=f'Duration: {min} minutes\n'
                                                     f'Preview: [Play now]({preview})\n',
                                         color=botsetup.geniusc)
                finishdl.set_author(name="Download finished",
                                    icon_url="https://apkdirectory.com/logos/genius-song-lyrics-038-more.png", )
                await ctx.send(embed=finishdl)
                await ctx.send(file=discord.File(f'genius_lyric.txt'))
        except:
            gnoly = discord.Embed(description=f'\n'
                                        f'If the song are available on [genius](https://genius.com)\n'
                                        f'click [bug report](mailto:contact@hqsartworks.me)',
                                  color=botsetup.error)
            gnoly.set_author(name=f'Error: Cant find song/artist: {arg1}',
                             icon_url='https://abload.de/img/15169975161ok74.gif')
            await ctx.send(embed=gnoly)
            await asyncio.sleep(5)
            await loadingly1.delete()

    @genius.error
    async def genius_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(embed=botsetup.noargs)



def setup(bot):
    bot.add_cog(fun(bot))
