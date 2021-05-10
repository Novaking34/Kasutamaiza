import discord
from discord.ext import commands
from discord.utils import get

class c210(commands.Cog, name="c210"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Halfmoon', aliases=['c210','Scorn_Operative_16'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Halfmoon',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348931.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Link/Effect (LIGHT)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='1 (2000/↘️)', inline=False)
        embed.add_field(name='Monster Effect', value='1 "Scorn Operative" monster with 2500 or more ATK\n(Quick Effect): You can target 1 "Manouevre -" card you control; return it to the hand, then this card gains the effects of that target until the End Phase, also, you can also activate these effects as Quick Effects. You cannot target a card, or activate the effects of a card with the same original name as the card targeted by this effect of "Scorn Operative - Halfmoon" for the rest of the Duel. You can only use this effect of "Scorn Operative - Halfmoon" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c210(bot))