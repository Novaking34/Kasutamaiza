import discord
from discord.ext import commands
from discord.utils import get

class c310(commands.Cog, name="c310"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Beauty\'s Lull', aliases=['c310'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Beauty\'s Lull')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361286.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Psychic/Xyz/Effect (DARK)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='4 (2600/1800)', inline=False)
        embed.add_field(name='Monster Effect', value='3 Level 4 monsters\nOnce per turn, you can detach 1 material from this card, then target 1 face-up monster your opponent controls; take control of it, but its effects are negated and this card cannot attack this turn. If this card leaves the field, send any monsters taken control by this card to the GY.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c310(bot))