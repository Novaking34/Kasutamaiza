import discord
from discord.ext import commands
from discord.utils import get

class c137(commands.Cog, name="c137"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Deadly_Plant_Beast', aliases=['c137'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Deadly Plant Beast',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334912.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Plant/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2350/1400)', inline=False)
        embed.add_field(name='Monster Effect', value='Fear them, for they lurk the darkness of the great forest. These plants hunt and destroy all they see, causing fear among all the forest dwellers.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c137(bot))