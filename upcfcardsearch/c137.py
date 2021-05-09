import discord
from discord.ext import commands
from discord.utils import get

class c137(commands.Cog, name="c137"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Dark_Minister_Iyu', aliases=['c137'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Dark Minister Iyu',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334905.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fiend/Normal (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (1950/1200)', inline=False)
        embed.add_field(name='Lore Text', value='For the reign of darkness is nigh, and the new Palace of the Pale Moonlight lurks. For Iyu does lurk in the shadows, awaiting for the perfect moment to ascend the throne.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c137(bot))