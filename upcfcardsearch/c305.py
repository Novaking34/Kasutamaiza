import discord
from discord.ext import commands
from discord.utils import get

class c305(commands.Cog, name="c305"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Demon\'s_Redemption', aliases=['c305'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Demon\'s Redemption',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361259.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Trap/Counter', inline=False)
        embed.add_field(name='Card Effect', value='If a monster(s) in your possession leaves the field because of an opponent\'s card effect: Pay 1500 LP; banish all card\'s from your opponent\'s GY. During your turn, if you control no Spells/Traps, you can activate this card from your hand.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c305(bot))