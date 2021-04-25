import discord
from discord.ext import commands
from discord.utils import get

class c30(commands.Cog, name="c30"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hidden_Treasure_Red_Quartz_Raccon', aliases=['c30','Hidden_Treasure_6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hidden Treasure Red Quartz Raccon',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321336.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1600/1900)', inline=False)
        embed.add_field(name='Monster Text', value='It is said that the only way to find the Hidden Treasure is to follow the Red Quartz Raccoon. It is known to steal other gems and horde them for because of their beauty. The other creatures of the Hidden Treasure are unaware that it is the Red Quartz Raccoon stealing the gems.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c30(bot))