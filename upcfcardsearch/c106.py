import discord
from discord.ext import commands
from discord.utils import get

class c106(commands.Cog, name="c106"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Golden_Statue_in_the_Sky', aliases=['c106'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Golden Statue in the Sky',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321563.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Fusion (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (1000/3500)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Fairy monster + 1 Rock monster', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c106(bot))