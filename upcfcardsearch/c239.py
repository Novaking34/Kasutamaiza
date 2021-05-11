import discord
from discord.ext import commands
from discord.utils import get

class c239(commands.Cog, name="c239"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Magia_Ignis', aliases=['c239', 'Magia_4'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Magia Ignis',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2359258.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Magia)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1500/1300)', inline=False)
        embed.add_field(name='Monster Effect', value='During your Main Phase: You can banish 1 "Magia" card from your hand or GY, then Special Summon 1 "Magia" monster from your hand. If this card is destroyed by a card effect: You can add 1 of your banished "Magia" cards to your hand. You can only use each effect of "Magia Ignis" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c239(bot))