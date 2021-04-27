import discord
from discord.ext import commands
from discord.utils import get

class c95(commands.Cog, name="c95"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Invasion_of_the_Dark_Army', aliases=['c95'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Invasion of the Dark Army',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321541.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Special Summon 2 DARK monsters from your hand or GY, then you take 300 points of damage x the total Levels of the monsters Special Summoned by this effect. Youi can only activate 1 "Invasion of the Dark Army" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c95(bot))