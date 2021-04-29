import discord
from discord.ext import commands
from discord.utils import get

class c110(commands.Cog, name="c110"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magista_the_Wizard_of_All_Divine_Magic', aliases=['c110'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magista the Wizard of All Divine Magic',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321570.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Fusion/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2100/2400)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Spellcaster + 1 DARK monster\nIf this card is Fusion Summoned using only Spellcaster monsters, this card cannot be targeted by your opponent’s Spell Cards or effects. (Quick Effect): You can banish 1 Spell from your GY; Set 1 Spell from your Deck with the same name as the banished card directly to the field, but you cannot activate cards, or the effects of cards, with that name for the rest of this turn. You can only activate the effects of "Magista the Wizard of All Divine Magic” once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c110(bot))