import discord
from discord.ext import commands
from discord.utils import get

class c277(commands.Cog, name="c277"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hex_of_Agoraphobia', aliases=['c277', 'Hex_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hex of Agoraphobia',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360759.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hex)', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='When an opponent\'s monster declares an attack: You can Tribute 1 monster you control; negate that attack, and if you do, return that monster to the hand, also, after that, if you Tributed a DARK monster to activate this card\'s effect, you can add 1 "Hex" Spell from your GY to your hand, except "Hex of Agoraphobia".', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c277(bot))