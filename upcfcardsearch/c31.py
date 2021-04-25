import discord
from discord.ext import commands
from discord.utils import get

class c31(commands.Cog, name="c31"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Hidden_Treasure_Mining_Site', aliases=['c31','Hidden_Treasure_7'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Hidden Treasure Mining Site',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321341.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='Once per turn, during your Main Phase 2, if you discarded 2 or more "Hidden Treasure" monsters: You can add 1 "Hidden Treasure" monster from your GY to your hand. You can only control 1 "The Hidden Treasure Mining Site". If this card is discarded: You can take 3 "Hidden Treasure" cards from your GY, your opponent chooses 1 to add to your hand, then shuffle the rest back into your Deck. You must control 2 or more Beast monsters or "Hidden Treasure" monsters to activate and resolve this effect of "The Hidden Treasure Mining Site".', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c31(bot))