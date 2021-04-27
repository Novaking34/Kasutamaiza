import discord
from discord.ext import commands
from discord.utils import get

class c56(commands.Cog, name="c56"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hemlock_Jar', aliases=['c56'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hemlock Jar',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321467.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (100/100)', inline=False)
        embed.add_field(name='Monster Effect', value='When this card is Normal Summoned: Banish 1 monster from your Deck. If this card leaves the field: Special Summon the monster banished by this card\'s effect, but its effects are negated, also you cannot Special Summon monsters for the rest of the turn. (Quick Effect): You can discard this card, then target 1 monster your opponent controls; reduce that monster\'s ATK/DEF by 1000, then, if that monster\'s ATK or DEF was reduced to 0, destroy that monster. You can only use each effect of "Hemlock Jar" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c56(bot))