import discord
from discord.ext import commands
from discord.utils import get

class c161(commands.Cog, name="c161"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Sheki_the_Mecha_Ninja_of_Time', aliases=['c161', 'of_Time_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Sheki the Mecha Ninja of Time',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2336293.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (of Time)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Normal (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='5 (1900/2300)', inline=False)
        embed.add_field(name='Lore Text', value='During the First Great War, many monsters were defenseless against the power that more formidable foes possesses. Unable to attend the Grand Gathering of the Kasutamaizers, a mysterious woman built Sheki to protect her town. Deemed a hero, Sheki guards the town and protects the weak, some say even he hides secrets... ', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c161(bot))