import discord
from discord.ext import commands
from discord.utils import get

class c278(commands.Cog, name="c278"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hex_of_Anomia', aliases=['c278', 'Hex_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hex of Anomia',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360768.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hex)', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Tribute 1 monster; Destroy 2 Spell/Trap cards your opponent controls, also, after that, if you Tributed a DARK monster to activate this card\'s effect, you can add 1 "Hex" Spell from your GY to your hand, except "Hex of Anomia".', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c278(bot))