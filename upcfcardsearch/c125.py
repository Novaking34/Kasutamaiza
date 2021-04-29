import discord
from discord.ext import commands
from discord.utils import get

class c125(commands.Cog, name="c125"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Flamestorm_Dragon', aliases=['c125'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Flamestorm Dragon',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334830.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dragon/Tuner/Normal (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (2000/1000)', inline=False)
        embed.add_field(name='Monster Effect', value='This little dragon will one day grow into a terrifying creature with unmatched combat abilities.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c125(bot))