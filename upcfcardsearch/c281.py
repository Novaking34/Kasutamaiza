import discord
from discord.ext import commands
from discord.utils import get

class c281(commands.Cog, name="c281"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hex_of_Thanatophobia', aliases=['c281', 'Hex_5'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hex of Thanatophobia',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360990.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hex)', inline=True)
        embed.add_field(name='Type', value='Spell/Equip', inline=False)
        embed.add_field(name='Card Effect', value='If the equipped monster is sent to the GY, its controller loses 1000 LP, also, if the equipped monster was a monster you controlled, you can add 1 "Hex" Spell from your GY to your hand, except "Hex of Thanatophobia".', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c281(bot))