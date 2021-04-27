import discord
from discord.ext import commands
from discord.utils import get

class c94(commands.Cog, name="c94"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Fortify_the_Defenses!', aliases=['c94'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Fortify the Defenses!',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321540.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='During your opponent\'s Battle Phase, if you control no monsters and you opponent declares a direct attack: Special Summon 2 Level 4 or lower monsters from your Deck or GY in Defense Position, but their effects are negated, also banish them when they leave the field. During the End Phase, if you control any monsters Special Summoned by this effect, take 700 damage for each.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c94(bot))