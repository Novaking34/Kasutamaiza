import discord
from discord.ext import commands
from discord.utils import get

class c101(commands.Cog, name="c101"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Cyber_Mage', aliases=['c101'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Cyber Mage',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321551.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Fusion/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (2000/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='1 Spellcaster monster + 1 Cyberse monster\nIf this card is destroyed by battle or card effect: You can Special Summon Spellcaster and/or Cyberse monsters from your GY whose total Levels equal this destroyed card\'s Level. You can only use the effects of "Cyber Mage" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c101(bot))