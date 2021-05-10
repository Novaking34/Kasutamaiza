import discord
from discord.ext import commands
from discord.utils import get

class c212(commands.Cog, name="c212"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Rosaria_Bladethorn', aliases=['c212'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Rosaria Bladethorn',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2356368.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Plant/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (500/500)', inline=False)
        embed.add_field(name='Monster Effect', value='If you control a Plant monster, you can Special Summon this card (from your hand). If this card is Tributed: You can draw 1 card, then discard 1 card. During the End Phase, if exactly 1 Spirit Monster you control would return to the hand by its own effect, you can return this card to your hand instead. You can only activate each effect of "Rosaria Bladethorn" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c212(bot))