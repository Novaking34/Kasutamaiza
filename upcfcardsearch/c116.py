import discord
from discord.ext import commands
from discord.utils import get

class c116(commands.Cog, name="c116"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Precise_Nullifier', aliases=['c116'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Precise Nullifier',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2328201.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1000/1000)', inline=False)
        embed.add_field(name='Monster Effect', value='You can discard this card and target 1 other monster in the GY; negate the effects of all monsters on the field with the same Type as that monster until the end of the turn. If this card is Normal or Special Summoned: You can destroy 1 monster on the field with its effects negated.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c116(bot))