import discord
from discord.ext import commands
from discord.utils import get

class c167(commands.Cog, name="c167"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Phantaclysmic_Arsonist', aliases=['c167', 'Phantaclysms_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Phantaclysmic Arsonist',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344770.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Plant/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (600/0)', inline=False)
        embed.add_field(name='Monster Effect', value='This card can attack directly. If this card is destroyed: During the End Phase, if this card is in the GY because it was destroyed and sent there this turn: You can Special Summon 1 "Phantaclysmic" monster from your Deck, except "Phantaclysmic Arsonist". You can only activate this effect of "Phantaclysmic Arsonist" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c167(bot))