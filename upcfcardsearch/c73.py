import discord
from discord.ext import commands
from discord.utils import get

class c73(commands.Cog, name="c73"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Aquacity', aliases=['c73'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Aquacity',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321494.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='All Aqua, Fish, and Sea-Serpent monsters gain 400 ATK/DEF, also all Pyro and Rock monsters lose 300 ATK/DEF. During the Draw Phase, instead of conducting their normal draw: The turn player can add from their GY to their hand, 1 card that lists "Aqua monster", "Fish monster", or "Sea Serpent monster" in it\'s text.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c73(bot))