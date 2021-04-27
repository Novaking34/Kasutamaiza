import discord
from discord.ext import commands
from discord.utils import get

class c92(commands.Cog, name="c92"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Cry_Cry_Shooting_Stars', aliases=['c92'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Cry Cry Shooting Stars',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321535.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Declare 1 Attribute; destroy all monsters currently on the field with that Attribute, then banish cards from the top of your Deck equal to the number of monsters destroyed by this effect, but effects of banished cards cannot be activated or resolved this turn. During the End Phase, if 6 or more cards are banished in a turn while this card is in the GY; Set this card directly from your GY to the field.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c92(bot))