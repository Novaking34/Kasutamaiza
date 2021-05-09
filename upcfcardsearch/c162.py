import discord
from discord.ext import commands
from discord.utils import get

class c162(commands.Cog, name="c162"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Colorful_Beast', aliases=['c162', 'The_Colorful_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Colorful Beast',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344688.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (The Colorful)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Normal (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Lore Text', value='It is said that after the world was reformed, a mystical beast created by angelic fairies of many colors appear. It might be weak now, but some say that its true power is hidden away by the creators themselves!', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c162(bot))