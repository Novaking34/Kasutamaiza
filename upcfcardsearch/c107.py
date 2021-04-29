import discord
from discord.ext import commands
from discord.utils import get

class c107(commands.Cog, name="c107"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Insectious_the_Fiend_Lord', aliases=['c107'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Insectious the Fiend Lord',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321566.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Insect/Fusion (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2200/1400)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Insect monster + 1 Fiend monster', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c107(bot))