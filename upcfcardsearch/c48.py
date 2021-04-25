import discord
from discord.ext import commands
from discord.utils import get

class c48(commands.Cog, name="c48"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='A_True_Catastrophe', aliases=['c48'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='A True Catastrophe',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321447.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fiend/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1500/1050)', inline=False)
        embed.add_field(name='Monster Effect', value='You can substitute this card for any 1 Fusion Material Monster. When you do this, the other Fusion Material Monster(s) must be the correct one(s). You can banish this card from your GY; Add 1 "Fusion" card or "Power Polymerization" from your GY to your hand. You can only use this effect of "A True Catastrophe" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c48(bot))