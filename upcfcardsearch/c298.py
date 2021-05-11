import discord
from discord.ext import commands
from discord.utils import get

class c298(commands.Cog, name="c298"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A_Simple_Tune', aliases=['c298'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A Simple Tune',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361151.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='At the start of your Main Phase 1: Draw 2 cards, then shuffle 1 card from your hand into the Deck. You cannot add cards from your Deck to your hand for the rest of the turn. You can only use 1 "A Simple Tune" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c298(bot))