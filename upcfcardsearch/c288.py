import discord
from discord.ext import commands
from discord.utils import get

class c288(commands.Cog, name="c288"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Lunar_Marionetter', aliases=['c288'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Lunar Marionetter',
                              color=0xA086B7)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361052.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Field/Fusion/Pendulum/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='6 (0/0) [0/0]', inline=False)
        embed.add_field(name='Pendulum Effect', value='This card\'s Pendulum Scale is equal to the number of Marionette Counters on this card.', inline=False)
        embed.add_field(name='Monster Effect', value='2 monsters with different Levels\nIf this card is Fusion Summoned: Negate the effects of all monsters on the field with the same Level as this card\'s Fusion Materials. Once per turn (Quick Effect): Target 1 other monster on the field; place this card in your Pendulum Zone, then place Marionette Counters on this card equal to the Level of the targeted monster.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c288(bot))