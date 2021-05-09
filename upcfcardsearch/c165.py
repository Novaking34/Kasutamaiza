import discord
from discord.ext import commands
from discord.utils import get

class c165(commands.Cog, name="c165"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Wan-Chi_the_Forest_Destroyer', aliases=['c165'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Wan-Chi the Forest Destroyer',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344698.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3=', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dragon/Normal (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2200/2400)', inline=False)
        embed.add_field(name='Lore Text', value='Be wary as you enter the Forest of the Faye Folk, for the legends have it that a Wan-Chi lurks, waiting for his time to destroy the forest. No one knows how Wan-Chi came to be, but it is said that during the First Great War, the Dragons themselves planned on wiping out the Fairy race, in fear of their enchanting magic.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c165(bot))