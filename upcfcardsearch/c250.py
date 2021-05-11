import discord
from discord.ext import commands
from discord.utils import get

class c250(commands.Cog, name="c250"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Mat\'Ergenu', aliases=['c250', 'Abyssal_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Mat\'Ergenu',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360275.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Flip/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1000/1000)', inline=False)
        embed.add_field(name='Monster Effect', value='FLIP: Target 1 face-up monster your opponent controls; take control of that monster until the End Phase.\nYou can banish this card from your GY, then target 1 "Abyssal" card in your GY; add it to your hand. You can only use each effect of "Abyssal Mat\'Ergenu" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c250(bot))