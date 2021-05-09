import discord
from discord.ext import commands
from discord.utils import get

class c197(commands.Cog, name="c197"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Southwind', aliases=['c197', 'Scorn_Operative_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Southwind',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348898.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Effect (WIND)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2000/1700)', inline=False)
        embed.add_field(name='Monster Effect', value='You can Tribute 1 "Manoeuvre -" Spell/Trap; Special Summon this card from your hand. You can Tribute this card and 1 card in the same column as this card, even if you do not control it; Special Summon 1 "Scorn Operative - Pyre" from your Extra Deck. You can only use this effect of "Scorn Operative - Southwind" once per turn. If this card inflicts battle damage to your opponent: You can return up to 3 "Scorn Operative" monsters from your GY to your Deck or Extra Deck.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c197(bot))