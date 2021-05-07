import discord
from discord.ext import commands
from discord.utils import get

class c197(commands.Cog, name="c197"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Starlight', aliases=['c197', 'Scorn_Operative_4'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Starlight',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348899.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1100/400)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is Summoned: You can activate 1 "Insurgent Resurgence" directly from your Deck. You can only use this effect of "Scorn Operative - Starlight" once per turn', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c197(bot))