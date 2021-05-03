import discord
from discord.ext import commands
from discord.utils import get

class c148(commands.Cog, name="c148"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Infectasaurous', aliases=['c148'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Infectasaurous',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336224.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dinosaur/Normal (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2450/2100)', inline=False)
        embed.add_field(name='Lore Text', value='The Infectasaurous is a rare breed of dinosaurs that hunt together in the wilds of the forest. It is said that these great lizard\'s skin is so tough, not even the strongest of topical poisons can harm them. They are even known to attack enemies while dipped in such toxins.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c148(bot))