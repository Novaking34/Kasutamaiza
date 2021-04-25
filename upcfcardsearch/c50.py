import discord
from discord.ext import commands
from discord.utils import get

class c50(commands.Cog, name="c50"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A-doraclay', aliases=['c50','A-dora_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A-doraclay',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321451.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (A-dora)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (300/200)', inline=False)
        embed.add_field(name='Monster Effect', value='Any battle damage involving this card is reduced to 0. If a Spell/Trap Card or effect is activated that would destroy 2 or more monsters you control (Quick Effect): You can Tribute this card; negate that effect, then Special Summon 1 "A-dora" monster from your hand or Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c50(bot))