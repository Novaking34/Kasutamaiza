import discord
from discord.ext import commands
from discord.utils import get

class c129(commands.Cog, name="c129"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Aqua_Marine_Battleship', aliases=['c129'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Aqua Marine Battleship',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334888.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Normal (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (2200/0)', inline=False)
        embed.add_field(name='Lore Text', value='Among the great reef, a patrolling battleship roams the sea. Called the Aqua Marine, all those who see this powerful ship quiver in fear.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c129(bot))