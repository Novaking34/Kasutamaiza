import discord
from discord.ext import commands
from discord.utils import get

class c105(commands.Cog, name="c105"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Flamana_the_Wizard_of_Tricks', aliases=['c105'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Flamana the Wizard of Tricks',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321560.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Pyro/Fusion/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (1800/600)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Pyro or Spellcaster monster + 1 FIRE monster\nIf this card is Fusion Summoned using only Pyro monsters, this card cannot be destroyed by Trap Cards or effects. (Quick Effect): You can banish 1 Trap from your GY; Set 1 Normal Trap from your GY directly to the field. You can only activate the effects of "Flamana the Wizard of Tricks" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c105(bot))