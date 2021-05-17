import discord
from discord.ext import commands
from discord.utils import get

class c313(commands.Cog, name="c313"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sakeira_Angel_of_Radiance', aliases=['c313'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sakeira, Angel of Radiance')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361296.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Xyz/Effect (LIGHT)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='0 (50/50)', inline=False)
        embed.add_field(name='Monster Effect', value='3 monsters Special Summoned from the Extra Deck with the same Level/Rank/Link Rating\n(This card\'s original Rank is always treated as 1.)\nAt the start of the Damage Step, if this card battles a monster: Destroy that monster. Once per turn (Quick Effect): You can detach 1 material from this card, then target 1 face-up monster on the field; it gains 3000 ATK/DEF, but its effects are negated.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c313(bot))