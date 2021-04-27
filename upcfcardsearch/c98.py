import discord
from discord.ext import commands
from discord.utils import get

class c98(commands.Cog, name="c98"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Beginning_of_a_New_End', aliases=['c98'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Beginning of a New End',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321545.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='During the Standby Phase: Excavate the top 3 cards of your Deck, then add 1 of those cards to your hand, send 1 of those cards to the GY shuffle the other into the Deck. For the rest of this turn after this card resolves, you cannot Special Summon monsters from your Extra Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c98(bot))