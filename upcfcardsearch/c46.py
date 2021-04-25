import discord
from discord.ext import commands
from discord.utils import get

class c46(commands.Cog, name="c46"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Divine_Justice_of_the_Kasutamaiza_Tribe', aliases=['c46','Kasutamaiza_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Divine Justice of the Kasutamaiza Tribe',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321420.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Kasutamaiza)', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='At the start of your Main Phase 1, you can activate this card: Pay 2000 LP; each player must discard 1 card from their hand, and if they cannot, send the top card of their Deck to the GY, also, after that, if each player controls at least 1 face-up monster, send 1 monster on each field to the GY. All battle damage dealt to your opponent is halved the turn you activate this card\'s effect.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c46(bot))