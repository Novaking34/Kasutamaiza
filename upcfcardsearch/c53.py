import discord
from discord.ext import commands
from discord.utils import get

class c53(commands.Cog, name="c53"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Beta_Beetle', aliases=['c53'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Beta Beetle',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321456.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Insect/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is destroyed by battle or card effect: Special Summon 1 "Beta Bettle" from your Deck. You can banish this card and 2 other "Beta Bettle" from your GY; Special Summon 1 Level 3 or lower monster from your Deck.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c53(bot))