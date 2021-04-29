import discord
from discord.ext import commands
from discord.utils import get

class c109(commands.Cog, name="c109"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magi_and_Mech', aliases=['c109'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magi and Mech',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321569.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Fusion (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2500/2400)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Spellcaster monster + 1 Machine monster', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c109(bot))