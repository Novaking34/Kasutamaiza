import discord
from discord.ext import commands
from discord.utils import get

class c147(commands.Cog, name="c147"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Hykamiko', aliases=['c147', 'A.I_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Hykamiko',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336220.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (A.I)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Pyro/Normal (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2050/1400)', inline=False)
        embed.add_field(name='Lore Text', value='With the new rise in technology, a mysterious force created a rift between the physical and technological world. Slowly slipping into the world of Kustomazi. Hykamiko, the driving force, bridged the world of modern media and TV to an ever so changing world. Even with advance magic, a new force deemed "A.I" began to spread, creating a new dynamic among the people.\n\n(This card is always treated as an "A.I" monster.)', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c147(bot))