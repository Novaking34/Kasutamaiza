import discord
from discord.ext import commands
from discord.utils import get

class c156(commands.Cog, name="c156"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Musaic_Robo-Knight', aliases=['c156', 'Musaic_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Musaic Robo-Knight',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336259.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Musaic)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Normal (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2650/2800)', inline=False)
        embed.add_field(name='Lore Text', value='It is said that the Musaic Tribe discovered a rare metal that allowed there instruments to never break. Using this metal, the Musaic\'s decided to create a robot that could play any instrument so their culture could live forever. However, during the First Great War, the robot was made into a music playing warrior, always yearning for a new tune.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c156(bot))