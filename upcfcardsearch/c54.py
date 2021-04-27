import discord
from discord.ext import commands
from discord.utils import get

class c54(commands.Cog, name="c54"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Chilly_Season_&_Snowy_Weather', aliases=['c54','Season_&_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Chilly Season & Snowy Weather',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321465.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Season &)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Tuner/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (200/1800)', inline=False)
        embed.add_field(name='Monster Effect', value='When a card or effect is activated that would negate the effect of a card(s) you control (Quick Effect): You can discard this card; negate that effect. Your opponent can reveal 2 cards from their hand and pay 500 LP to negate this effect. If you have no monsters with "Season &" in its name in your GY, this effect cannot be negated. You can only use the effect of "Chilly Season & Snowy Weather" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c54(bot))