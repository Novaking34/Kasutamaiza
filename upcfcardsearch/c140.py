import discord
from discord.ext import commands
from discord.utils import get

class c140(commands.Cog, name="c140"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Fiendish_Key_of_the_Underworld', aliases=['c140'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Fiendish Key of the Underworld',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336030.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fiend/Normal (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Lore Text', value='No one knows where the key opens, but some say when its discovered, the demon king Luthro will reawaken from his dark slumber.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c140(bot))