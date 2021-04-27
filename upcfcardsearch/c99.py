import discord
from discord.ext import commands
from discord.utils import get

class c99(commands.Cog, name="c99"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Unstable_Bond', aliases=['c99'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Unstable Bond',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321546.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='When exactly 1 Fusion Monster is Fusion Summoned: Return that monster to the Extra Deck. The controller of that Fusion Monster can banish all Fusion Materials used for the Fusion Summon of that monster from the GY, face down, to negate this effect.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c99(bot))