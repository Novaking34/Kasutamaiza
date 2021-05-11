import discord
from discord.ext import commands
from discord.utils import get

class c237(commands.Cog, name="c237"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Amica', aliases=['c237', 'Magia_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Amica',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359254.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1100/1900)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card in your possession is destroyed: You can Special Summon 1 Level 4 or lower "Magia" monster from your Deck in Defense Position. You can only use each effect of "Magia Amica" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c237(bot))