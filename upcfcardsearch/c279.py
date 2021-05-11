import discord
from discord.ext import commands
from discord.utils import get

class c279(commands.Cog, name="c279"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hex_of_Arthrophobia', aliases=['c279', 'Hex_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hex of Arthrophobia',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360772.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hex)', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Discard 1 card and target 1 face-up monster on the field; that monster\'s original ATK becomes halved until the end of this turn. During your End Phase, if a DARK monster you control was sent to the GY the turn you activated this card: You can add 1 "Hex" Spell from your GY to your hand, except "Hex of Arthrophobia".', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c279(bot))