import discord
from discord.ext import commands
from discord.utils import get

class c40(commands.Cog, name="c40"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Kasutamaiza_the_Creator', aliases=['c40'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Kasutamaiza the Creator',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321408.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Kasutamaiza)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Divine-Beast/Effect (DIVINE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='12 (4000/4000)', inline=False)
        embed.add_field(name='Monster Effect', value='Cannot be Special Summoned or Normal Set. Requires 3 Tributes to Tribute Summon. Cannot attack the turn it is Summoned. While you have 1000 or less LP, this card is unaffected by other card effects. If this card is Normal Summoned: You can add 1 card from your Deck or GY to your hand. You cannot activate other cards or effects, or Summon a monster(s) for the rest of the turn after you activate this effect. You can only use this effect of "Kasutamaiza the Creator" once per Duel.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c40(bot))