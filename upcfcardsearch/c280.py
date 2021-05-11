import discord
from discord.ext import commands
from discord.utils import get

class c280(commands.Cog, name="c280"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hex_of_Claustrophobia', aliases=['c280', 'Hex_4'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hex of Claustrophobia',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360775.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hex)', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='Select 2 unoccupied Main Monster Zones on each player\'s field. Neither player can use the selected zones, then, if you only control DARK monsters, you can add 1 "Hex" Spell from your GY to your hand, except "Hex of Claustrophobia".', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c280(bot))