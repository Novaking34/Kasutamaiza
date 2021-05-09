import discord
from discord.ext import commands
from discord.utils import get

class c139(commands.Cog, name="c139"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='DracoGuard_of_the_Gate', aliases=['c139'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='DracoGuard of the Gate',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2334912.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Wyrm/Normal (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (3000/2800)', inline=False)
        embed.add_field(name='Lore Text', value='In order to prevent the living and dead from creating chaos once more, the Dragon race offered their champion to stand guard at the Gates between the two worlds. Standing tall, only the most clever of the bunch can get past his mighty gaze.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c139(bot))