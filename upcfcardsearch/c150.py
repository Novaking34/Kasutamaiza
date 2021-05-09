import discord
from discord.ext import commands
from discord.utils import get

class c150(commands.Cog, name="c150"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Jetstream_Time_Dragon', aliases=['c150'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Jetstream Time Dragon',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336225.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dragon/Toon/Normal (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2200/2000)', inline=False)
        embed.add_field(name='Lore Text', value='From all across the world, this dragon has a grand set of knowledge to him. However, a strange phenomenon caused it to be trapped in between a time paradox. Forever traveling, this dragon ushers in the new frontier of monsters every 100 years.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c150(bot))