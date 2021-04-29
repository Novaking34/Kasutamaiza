import discord
from discord.ext import commands
from discord.utils import get

class c102(commands.Cog, name="c102"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Cyber_Mage_V2', aliases=['c102'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Cyber Mage V2',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321552.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Fusion/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2400/2500)', inline=False)
        embed.add_field(name='Monster Effect', value='Must first be Special Summoned (from your Extra Deck) by Tributing 1 "Cyber Mage" you control with 4 or more Spell Counters. Once per turn: You can banish up to 2 Level 3 or lower Spellcaster or Cyberse monsters from your GY; add 1 Spellcaster or Cyberse monster from your GY to your hand, whose total Levels equal the combined Levels of the banished monsters. Once per turn, during the End Phase of the turn this card on the field was destroyed: You can Special Summon 1 "Cyber Mage" from your GY.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c102(bot))