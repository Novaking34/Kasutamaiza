import discord
from discord.ext import commands
from discord.utils import get

class c244(commands.Cog, name="c244"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Dance_Metum', aliases=['c244', 'Magia_9'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Dance Metum',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359462.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type', value='Spell/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Target 2 other cards on the field, including 1 "Magia" card; destroy them. You can only activate 1 "Magia Dance Metum" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c244(bot))