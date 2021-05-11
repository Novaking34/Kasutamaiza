import discord
from discord.ext import commands
from discord.utils import get

class c276(commands.Cog, name="c276"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Distasta_Master_Tempestatis', aliases=['c276', 'Distasta_Master_7'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Distasta Master Tempestatis',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360726.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Distasta Master)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Aqua/Fusion/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (1700/2100)', inline=False)
        embed.add_field(name='Monster Effect', value='"Vir the True Elementalist" + 1 WATER monster\nThis card cannot be destroyed by battle or by the card effects of monsters, except those of an EARTH monster. (Quick Effect): You can declare 1 card type (Monster, Spell, or Trap), then excavate the top card of your Deck; if the declared card type is revealed, add 1 card of the declared card type from your GY to your hand, then if your opponent has more cards in their hand than you do, draw 1 card, also, after that, place the excavated card on the bottom of your Deck. If this card is destroyed and sent to the GY: You can Special Summon 1 Level 5 or lower WATER monster that is banished or in your GY, except "Distasta Master Tempestatis", but its effects are negated this turn. You can only activate each effect of "Distasta Master Tempestatis" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c276(bot))