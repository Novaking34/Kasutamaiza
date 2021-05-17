import discord
from discord.ext import commands
from discord.utils import get

class c316(commands.Cog, name="c316"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Alexander_the_Impenetrable', aliases=['c316'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Alexander the Impenetrable',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2367727.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Link/Effect (DARK)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='3 (3200/↙️⬇️➡️)', inline=False)
        embed.add_field(name='Monster Effect', value='2+ Effect Monsters\nCannot attack. This effect cannot be negated. Once per turn, when a card or effect is activated that targets a monster(s) you control (Quick Effect): You can discard 1 card; negate the activation.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c316(bot))