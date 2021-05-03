import discord
from discord.ext import commands
from discord.utils import get

class c146(commands.Cog, name="c146"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Gummi', aliases=['c146'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Gummi',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336215.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2050/2550)', inline=False)
        embed.add_field(name='Lore Text', value='From the creators of the Toontastic Kingdom, meet Gummi the machine that smiles. He provides so much joy, even the other Toons don\'t bother and fight him.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c146(bot))