import discord
from discord.ext import commands
from discord.utils import get

class c145(commands.Cog, name="c145"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Grublin_Whoguard', aliases=['c145', 'Grublin_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Grublin Whoguard',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336213.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Grublin)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Toon/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1200/1700)', inline=False)
        embed.add_field(name='Lore Text', value='When the Great Food War first began, mages and chefs worked together in order to stop the dark forces of the Hanger tribe by creating golems of stale bread. The Grublin Whoguards are strong and sentinel, unmoved and powerful to keep the Grublin Kingdom protected.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c145(bot))