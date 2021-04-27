import discord
from discord.ext import commands
from discord.utils import get

class c63(commands.Cog, name="c63"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sir_Noel_Apprentice_of_the_Augmentist', aliases=['c63', 'Augmentist_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sir Noel, Apprentice of the Augmentist',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321478.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Augmentist)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Tuner/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (500/600)', inline=False)
        embed.add_field(name='Monster Effect', value='If you draw this card: You can reveal this card, then target 1 face-up monster and declare an Attribute; that monster becomes the declared Attribute. Once per turn: You can target 1 face-up monster on the field with a Level, then declare 1 Level from 1 to 12; while this card is face-up on the field, that monster becomes the declared Level.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c63(bot))