import discord
from discord.ext import commands
from discord.utils import get

class c77(commands.Cog, name="c77"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Fuel_the_Fiend', aliases=['c77'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Fuel the Fiend',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321501.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='Once per turn: You can Tribute 1 monster you control; Gain LP equal to that monster\'s original ATK.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c77(bot))