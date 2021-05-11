import discord
from discord.ext import commands
from discord.utils import get

class c275(commands.Cog, name="c275"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Distasta_Master_Turbinis-Vasti', aliases=['c275', 'Distasta_Master_6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Distasta Master Turbinis-Vasti',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360719.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Distasta Master)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Winged Beast/Fusion/Effect (WIND)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2300/1700)', inline=False)
        embed.add_field(name='Monster Effect', value='"Vir the True Elementalist" + 1 WIND monster\nThis card cannot be destroyed by battle or by the card effects of monsters, except those of a FIRE monster. (Quick Effect): You can declare 1 card type (Monster, Spell, or Trap), then excavate the top card of your Deck; if the declared card type is revealed, shuffle 1 card on the field to the Deck, and if you only control 1 monster, shuffle 1 card in your opponent\'s hand back into their Deck, also, after that, place the excavated card on the bottom of your Deck. If this card is destroyed and sent to the GY: You can Special Summon 1 Level 5 or lower WIND monster that is banished or in your GY, except "Distasta Master Turbinis-Vasti", but its effects are negated this turn. You can only activate each effect of "Distasta Master Turbinis-Vasti" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c275(bot))