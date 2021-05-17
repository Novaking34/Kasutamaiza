import discord
from discord.ext import commands
from discord.utils import get

class c318(commands.Cog, name="c318"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Aquamarina', aliases=['c318'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Aquamarina',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2367739.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Link/Effect (WATER)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='2 (1600/⬇️↗️)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Rock monsters\nIf a Rock monster(s) is banished: You can target 1 Spell/Trap your opponent controls; destroy it. If this card is banished: You can target 1 card in either GY; banish it. You can only use each effect of "Aquamarina" once per turn', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c318(bot))