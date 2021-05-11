import discord
from discord.ext import commands
from discord.utils import get

class c300(commands.Cog, name="c300"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Flutist_of_Mysticism', aliases=['c300'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Flutist of Mysticism',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361166.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 face-up Spell/Trap that was not previously activated this Chain; negate its effects until the end of the next turn. The targeted card cannot activate its effects in response to this card.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c300(bot))