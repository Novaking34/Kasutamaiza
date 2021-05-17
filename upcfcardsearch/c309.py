import discord
from discord.ext import commands
from discord.utils import get

class c309(commands.Cog, name="c309"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Titan\'s_Graveyard', aliases=['c309'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Titan\'s Graveyard',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361273.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Continous', inline=False)
        embed.add_field(name='Card Effect', value='Discard 1 Rock monster; send up to 2 Rock monsters from your Deck to your GY. You can banish this card from your GY; Special Summon 1 Rock monster from your GY. You can only use 1 effect of "The Titan\'s Graveyard" per turn, and only once that turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c309(bot))