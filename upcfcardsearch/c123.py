import discord
from discord.ext import commands
from discord.utils import get

class c123(commands.Cog, name="c123"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Clay_Soldier', aliases=['c123'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Clay Soldier',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334814.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (1200/200)', inline=False)
        embed.add_field(name='Monster Effect', value='A formidable foot soldier whose blood boils in combat. He waged war against the man who desecrated the graves of his family.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c123(bot))