import discord
from discord.ext import commands
from discord.utils import get

class c269(commands.Cog, name="c269"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Vir_the_True_Elementalist', aliases=['c269', 'Elementalist_1', 'Distasta_Master_1'])    
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Vir the True Elementalist',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360695.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Elementalist/Distasta Master)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Normal (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (1200/950)', inline=False)
        embed.add_field(name='Lore Text', value='Some say that whenever a disaster occurs, Vir is near by practicing his magic. However, if Vir ever learns the secrets of the Book of Natural Disasters, with knowledge of the ancient scriptures, he will be able to tame the Distasta Masters and bring the world into a new age of doom.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c269(bot))