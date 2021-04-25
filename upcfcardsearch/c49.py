import discord
from discord.ext import commands
from discord.utils import get

class c49(commands.Cog, name="c49"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A-dorabelle', aliases=['c49','A-dora_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A-dorabelle',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321449.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (A-dora)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fish/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1200/1200)', inline=False)
        embed.add_field(name='Monster Effect', value='During your Main Phase 1: You can Special Summon 1 "A-dora" monster from your hand or GY in Attack Position, then if you only control "A-dora" monsters, return 1 card on the field to the Deck. For the rest of this turn, you cannot Special Summon monsters from your Deck or GY. You can only activate the effects of "A-dorabelle" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c49(bot))