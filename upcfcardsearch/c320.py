import discord
from discord.ext import commands
from discord.utils import get

class c320(commands.Cog, name="c320"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Gear_of_Eternity', aliases=['c320'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Gear of Eternity',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2367748.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Link/Effect (LIGHT)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='2 (1700/⬇️➡️)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Machine monsters\nIf this card is Link Summoned: Target 1 Machine monster in your GY; add it to your hand. During the Battle Phase, neither player can target or destroy other Machine monsters you control with card effects. You can only Special Summon "Gear of Eternity(s)" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c320(bot))