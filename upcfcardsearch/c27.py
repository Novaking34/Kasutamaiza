import discord
from discord.ext import commands
from discord.utils import get

class c27(commands.Cog, name="c27"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hidden_Treasure_Jasper_Armadillo', aliases=['c27','Hidden_Treasure_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hidden Treasure Jasper Armadillo',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321329.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (100/2100)', inline=False)
        embed.add_field(name='Monster Effect', value='You can reveal this card in your hand: your opponent randomly chooses 1 card from your entire hand, then you discard the chosen card. Then, if the discarded card was not "Hidden Treasure Jasper Armadillo", Special Summon 1 "Hidden Treasure Jasper Armadillo" from your hand, and if you have 2 or less cards in your hand, draw 1 card, also, for the rest of the turn, you cannot Special Summon monsters, except Beast monsters. If this card is discarded: You can target cards on the field, up to the number of Beast monsters in your GY, except "Hidden Treasure Jasper Armadillo(s)" (max. 2); destroy those targets. You can only use each effect of "Hidden Treasure Jasper Armadillo" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c27(bot))