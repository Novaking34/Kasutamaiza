import discord
from discord.ext import commands
from discord.utils import get

class c205(commands.Cog, name="c205"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Manoeuvre_Salt_the_Earth', aliases=['c205', 'Scorn_Operative_11'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Manoeuvre - Salt the Earth',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348914.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='If a "Scorn Operative" monster you control declares an attack, or is attacked: You can draw 1 card. You can only use this effect of "Manoeuvre - Salt the Earth" up to twice per turn. If you activate and resolve the effect of "Manoeuvre - Synthetic Motion": You can draw 1 card. You can only control 1 "Manoeuvre - Salt the Earth".', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c205(bot))