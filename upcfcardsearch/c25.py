import discord
from discord.ext import commands
from discord.utils import get

class c25(commands.Cog, name="c25"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hidden_Treasure_Emerald_Peacock', aliases=['c25'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hidden Treasure Emerald Peacock',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321323.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast/Effect (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1900/0)', inline=False)
        embed.add_field(name='Monster Effect', value='You can reveal this card in your hand: your opponent randomly chooses 1 card from your entire hand, then you discard the chosen card. Then, if the discarded card was not "Hidden Treasure Emerald Peacock", Special Summon 1 "Hidden Treasure Emerald Peacock" from your hand, and if you have 2 or less cards in your hand, draw 1 card, also, for the rest of the turn, you cannot Special Summon monsters, except Beast monsters. If this card is discarded: Beast monsters you control gain 1000 ATK/DEF, also, after that, add 1 "Hidden Treasure" monster from your GY to your hand. You can only use each effect of "Hidden Treasure Emerald Peacock" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c25(bot))