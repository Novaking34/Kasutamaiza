import discord
from discord.ext import commands
from discord.utils import get

class c224(commands.Cog, name="c224"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sandwoman_Trickster_of_the_Night', aliases=['c224'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sandwoman, Trickster of the Night',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359071.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='(Quick Effect): You can discard this card, then target 1 face-up monster on each field; change them to face-down Defense Position. You can banish this card from your GY, then target 1 face-down monster on the field; change it to face-up Attack or Defense Position. You can only use 1 "Sandwoman, Trickster of the Night" effect per turn, and only once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c224(bot))