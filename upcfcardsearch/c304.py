import discord
from discord.ext import commands
from discord.utils import get

class c304(commands.Cog, name="c304"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Tree_of_Memories', aliases=['c304'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Tree of Memories',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361249.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Pay 2000 LP then target 1 face-up card on the field; negate that target\'s face-up effects for the rest of the turn. Neither player can activate cards or effects in response to this card\'s activation.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c304(bot))