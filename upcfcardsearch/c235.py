import discord
from discord.ext import commands
from discord.utils import get

class c235(commands.Cog, name="c235"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Dark_Dancer_Aliya', aliases=['c235'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Dark Dancer Aliya',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359220.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Link/Effect (DARK)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='2 (1700/⬆️⬇️)', inline=False)
        embed.add_field(name='Monster Effect', value='2 DARK and/or Fairy monsters\nIf this card points to a monster(s): You can change the control of all monsters this card points to, then, if 2 monsters switched control by this card\'s effect, you can draw 1 card. You can only use the effect of "Dark Dancer Aliya" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c235(bot))