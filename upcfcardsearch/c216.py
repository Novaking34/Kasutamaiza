import discord
from discord.ext import commands
from discord.utils import get

class c216(commands.Cog, name="c216"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Automaton_Doll_&_Winter_Lights', aliases=['c216'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Automaton Doll & Winter Lights',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2356400.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Tuner/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (0/1800)', inline=False)
        embed.add_field(name='Monster Effect', value='During damage calculation, if your monster is battling an opponent\'s monster with higher ATK (Quick Effect): You can discard this card; your battling monster gains ATK/DEF equal to the ATK of the opponent\'s monster it is battling, until the end of the turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c216(bot))