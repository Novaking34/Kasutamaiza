import discord
from discord.ext import commands
from discord.utils import get

class c144(commands.Cog, name="c144"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Goden_the_Wolf_Prince', aliases=['c144'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Goden the Wolf Prince',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336209.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Beast-Warrior/Normal (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1300/1050)', inline=False)
        embed.add_field(name='Lore Text', value='Though he is a young prince today, Goden leads the fiercest pack of wolf in the land. No creature can best his authority, and the animal respect his rule.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c144(bot))