import discord
from discord.ext import commands
from discord.utils import get

class c69(commands.Cog, name="c69"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Windy_Season_&_Turbulent_Weather', aliases=['c69','Season_&_4'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Windy Season & Turbulent Weather',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321486.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Season &)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Tuner/Effect (WIND)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (200/1800)', inline=False)
        embed.add_field(name='Monster Effect', value='If your opponent adds a card(s) to their hand, except by drawing them (Quick Effect): You can discard this card; return 1 card in your opponent\'s hand to their Deck, then, if you have 5 or more "Season &" monster in your GY, return 1 card on the field to the Deck. Your opponent can return 1 card from their field to their hand to negate this card\'s effect, but they cannot activate that card this turn, also, it must remain revealed this turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c69(bot))