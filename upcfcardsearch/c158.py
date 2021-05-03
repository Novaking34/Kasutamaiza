import discord
from discord.ext import commands
from discord.utils import get

class c158(commands.Cog, name="c158"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Right_Leg_of_Automaton', aliases=['c158', 'Automaton_5'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Right Arm of Automaton',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336273.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Automaton)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Lore Text', value='The right leg to a gigantic mech, it it said that if you gather the other 4 pieces to this machine, a great mech of extraordinary power can be created.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c158(bot))