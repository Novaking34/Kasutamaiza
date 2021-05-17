import discord
from discord.ext import commands
from discord.utils import get

class c312(commands.Cog, name="c312"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Maiden_of_Vengeance', aliases=['c312'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Maiden of Vengeance')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361293.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Xyz/Effect (DARK)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='2 (1800/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='3 Level 2 monsters\nIf this card is Xyz Summoned: You can target 1 card in either player\'s GY; attach it to this card as material. Once per turn, when your opponent activates a card or effect (Quick Effect): You can detach 2 materials from this card; negate that effect, and if you do, this card gains 500 ATK.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c312(bot))