import discord
from discord.ext import commands
from discord.utils import get

class c154(commands.Cog, name="c154"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Machine_Lord_Knight', aliases=['c154', 'Machine_Lord_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Machine Lord Knight',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336251.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Machine Lord)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2000/2100)', inline=False)
        embed.add_field(name='Lore Text', value='Forever in a battle with the Timekeepers, the Machine Lord empire grows stronger by the day. With the power of the Machine Lord Knight\'s, it is said nothing is impossible.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c154(bot))