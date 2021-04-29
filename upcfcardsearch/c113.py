import discord
from discord.ext import commands
from discord.utils import get

class c113(commands.Cog, name="c113"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Zombo_Draco-Lord', aliases=['c113'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Zombo Draco-Lord',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321576.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Zombie/Fusion (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2550/1850)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Zombie monster + 1 Dragon monster', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c113(bot))