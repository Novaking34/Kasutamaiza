import discord
from discord.ext import commands
from discord.utils import get

class c249(commands.Cog, name="c249"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Malum', aliases=['c249', 'Magia_14'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Malum',
                              color=0x00008B)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359476.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fiend/Link/Effect (DARK)', inline=False)
        embed.add_field(name='Link Rating (ATK/Link Arrows)', value='1 (0/⬇️)', inline=False)
        embed.add_field(name='Monster Effect', value='1 "Magia" monster\n(Quick Effect): You can Tribute this card; reveal 1 "Maestitia" monster from your Extra Deck, and if you do, banish Fusion Materials listed on it from your GY, except "Magia Malum", then Special Summon that monster, ignoring its Summoning Conditions. You can only use this effect of "Magia Malum" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c249(bot))