import discord
from discord.ext import commands
from discord.utils import get

class c321(commands.Cog, name="c321"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Octavia_the_Symphony_of_Ruin', aliases=['c321'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Octavia, the Symphony of Ruin',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2367752.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Link/Effect (LIGHT)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='4 (2700/⬅️⬇️↘️➡️)', inline=False)
        embed.add_field(name='Monster Effect', value='2+ Effect Monsters\nCannot be Special Summoned during your opponent\'s turn. If this card is Link Summoned: You can target cards on the field, up to the number of Link Materials used for this card\'s Link Summon; destroy them, and if you do, inflict 200 damage to your opponent for each card destroyed by this effect, but this card cannot attack this turn. You can only use this effect of "Octavia, the Symphony of Ruin" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c321(bot))