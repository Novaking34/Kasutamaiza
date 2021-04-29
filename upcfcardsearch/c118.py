import discord
from discord.ext import commands
from discord.utils import get

class c118(commands.Cog, name="c118"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Ascent_Against_the_Heavens', aliases=['c118'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Ascent Against the Heavens',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2328206.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 monster your opponent controls and 1 monster in your GY with less ATK than that monster; Special Summon that monster from your GY in Attack Position, and if you do, the opponent\'s monster loses ATK equal to the ATK of the Summoned monster.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c118(bot))