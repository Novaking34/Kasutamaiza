import discord
from discord.ext import commands
from discord.utils import get

class c41(commands.Cog, name="c41"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Void_of_Creation', aliases=['c41'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Void of Creation',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321411.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Divine-Beast/Effect (DIVINE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='Cannot be Normal Summoned/Set. Must first be Special Summoned by returning 1 Normal Summoned monster you control to your hand. Cannot be destroyed by card effects, also both players take battle damage from attacks involving this card. You can banish this card and 2 other "The Void of Creation" from your GY; Special Summon 3 "Creation Tokens" (Divine-Beast/DIVINE/Level 1/ATK 0/DEF 0), then if you have no cards in your hand, you can add 1 "Kasutamaiza the Creator" from your Deck to your hand. You can only activate this effect of "The Void of Creation" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c41(bot))