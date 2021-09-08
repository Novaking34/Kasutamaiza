import discord
from discord.ext import commands
from discord.utils import get

class c52(commands.Cog, name="c52"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Accursed_Jar', aliases=['c52'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Accursed Jar',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321455.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is destroyed by battle: Change the monster that destroyed this card to face down Defense Position, or if it was a Link Monster, destroy it. Until the end of your opponent next Battle Phase, that monster cannot changes it battle position. If this card sent from the field to the GY, banish it face down.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c52(bot))