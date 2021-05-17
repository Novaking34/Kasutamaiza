import discord
from discord.ext import commands
from discord.utils import get

class c319(commands.Cog, name="c319"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Butterfly_Queen_Serrieri', aliases=['c319'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Butterfly Queen Serrieri',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2367743.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Insect/Link/Effect (EARTH)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='2 (1700/⬇️➡️)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Non-Link Effect Monsters\nCannot be used as Link Material. Once per turn (Quick Effect): You can discard 1 card, then target 1 other Attack Position monster on each side of the field; banish them until the End Phase. During your Main Phase, except the turn this card was sent to the GY: You can banish 1 monster you control; Special Summon this card from your GY, but banish it when it leaves the field.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c319(bot))