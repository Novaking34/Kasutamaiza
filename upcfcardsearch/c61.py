import discord
from discord.ext import commands
from discord.utils import get

class c61(commands.Cog, name="c61"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Rainy_Season_&_Stormy_Weather', aliases=['c61','Season_&_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Rainy Season & Stormy Weather',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321475.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Season &)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Tuner/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (200/1800)', inline=False)
        embed.add_field(name='Monster Effect', value='When your opponent activates the effects of a Spell/Trap Card that was already face-up on the field the previous turn (Quick Effect): You can discard this card; negate the activation, then, if you have 5 or more "Season &" monsters in your GY, destroy 1 Spell/Trap card on the field. Your opponent can discard 1 card of the same Type (Spell or Trap) to negate this card\'s effect.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c61(bot))