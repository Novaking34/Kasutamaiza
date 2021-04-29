import discord
from discord.ext import commands
from discord.utils import get

class c114(commands.Cog, name="c114"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Ghost_Maiden_Ana', aliases=['c114'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Ghost Maiden Ana',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321578.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Psychic/Tuner/Synchro/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (200/1800)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Psychic Tuner + 1+ non Tuner monsters\nIf this card is Synchro Summoned: Place 1 card from your GY on the bottom of the Deck. Once per turn: You can pay 800 LP; place 1 card from your GY on the bottom of the Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c114(bot))