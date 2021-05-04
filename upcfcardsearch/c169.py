import discord
from discord.ext import commands
from discord.utils import get

class c169(commands.Cog, name="c169"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Phantaclysmic_Samurai', aliases=['c169', 'Phantaclysms_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Phantaclysmic Samurai',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344790.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Warrior/Effect (WIND)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='2 (1000/0)', inline=False)
        embed.add_field(name='Monster Effect', value='This card can attack directly. If this card is Summoned or destroyed: You can Special Summon 1 "Phantaclysmic" monster from your hand or GY, except "Phantaclysmic Samurai". You can only activate this effect of "Phantaclysmic Samurai" once per turn and only if you haven\'t activated this effect last turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c169(bot))