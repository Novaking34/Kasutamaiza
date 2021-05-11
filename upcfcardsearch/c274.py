import discord
from discord.ext import commands
from discord.utils import get

class c274(commands.Cog, name="c274"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Distasta_Master_Terraemotus', aliases=['c274', 'Distasta_Master_5'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Distasta Master Terraemotus',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360717.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Distasta Master)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Fusion/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (1000/2500)', inline=False)
        embed.add_field(name='Monster Effect', value='"Vir the True Elementalist" + 1 EARTH monster\nThis card cannot be destroyed by battle or by the card effects of monsters, except those of a WIND monster. (Quick Effect): You can declare 1 card type (Monster, Spell, or Trap), then excavate the top card of your Deck; if the declared card type is revealed destroy 1 card your opponent controls, and if you do, you can destroy 1 card on the field that is the same card type as the declared card, also, after that, place the excavated card on the bottom of your Deck. If this card is destroyed and sent to the GY: You can Special Summon 1 Level 5 or lower EARTH monster that is banished or in your GY, except "Distasta Master Terraemotus", but its effects are negated this turn. You can only activate each effect of "Distasta Master Terraemotus" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c274(bot))