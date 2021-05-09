import discord
from discord.ext import commands
from discord.utils import get

class c199(commands.Cog, name="c199"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Nightbloom', aliases=['c199', 'Scorn_Operative_5'])    
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Nightbloom',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348901.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (2000/100)', inline=False)
        embed.add_field(name='Lore Text', value='Without question, she was called, and there was no way for her to forsake it. How long had they been preparing for this? Truth as it was, it was long since they\'d been prepared for it. It was only now time for the game to begin. So she went to war, played her part with the willingness of nothing else.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c199(bot))