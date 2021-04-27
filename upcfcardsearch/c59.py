import discord
from discord.ext import commands
from discord.utils import get

class c59(commands.Cog, name="c59"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Lady_Lyra_Queen_of_the_Augmentist', aliases=['c59', 'Augmentist_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Lady Lyra, Queen of the Augmentist',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321470.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Augmentist)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Tuner/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (500/600)', inline=False)
        embed.add_field(name='Monster Effect', value='If you draw this card: You can reveal this card, then target 1 face-up monster and declare an Attribute; that monster becomes the declared Attribute. Once per turn: You can target 1 face-up monster on the field, then declare 1 Type; while this card is face-up on the field, that monster becomes the declared Type.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c59(bot))