import discord
from discord.ext import commands
from discord.utils import get

class c152(commands.Cog, name="c152"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Living_Bullet', aliases=['c152'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Living Bullet',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336244.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Normal (EARTH)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2850/2000)', inline=False)
        embed.add_field(name='Lore Text', value='With nothing in its path, this bullet is always known to find its mark. People try to capture and control this bullet, but no man, beast or entity has yet been able to tame the Living Bullet.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c152(bot))