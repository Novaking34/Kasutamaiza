import discord
from discord.ext import commands
from discord.utils import get

class c121(commands.Cog, name="c121"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Beam_Mage', aliases=['c121'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Beam Mage',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334807.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Normal (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1800/1100)', inline=False)
        embed.add_field(name='Lore Text', value='A Beam Mage is a member of a closed community of wizards. Children with innate abilities are initiated and taught to harness their powers until they could conjure blasts without wands.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c121(bot))