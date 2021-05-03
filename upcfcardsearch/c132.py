import discord
from discord.ext import commands
from discord.utils import get

class c132(commands.Cog, name="c132"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Cyberse-Cop', aliases=['c132'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Cyberse-Cop',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334898.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Normal (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (3000/2500)', inline=False)
        embed.add_field(name='Lore Text', value='Constantly on guard, the Cyberse-Cops stop at nothing to ensure truth and justice is upheld. They are constanly updated on the crime in the area and are swift in taking action.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c132(bot))