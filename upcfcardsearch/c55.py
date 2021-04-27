import discord
from discord.ext import commands
from discord.utils import get

class c55(commands.Cog, name="c55"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Cladio_the_Final_Boy', aliases=['c55'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Cladio the Final Boy',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321466.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (200/1400)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is sent directly from the Deck to the GY while you control no monsters: You can Special Summon this card, but it cannot be used as Link Material. You can only use this effect of "Cladio the Final Boy" once per turn. Once per turn, if you control no other cards: You can Special Summon 1 Level 3 or lower monster from your GY, but banish it when it leaves the field.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c55(bot))