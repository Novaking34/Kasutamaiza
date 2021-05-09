import discord
from discord.ext import commands
from discord.utils import get

class c183(commands.Cog, name="c183"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Devoted_Servant_Nana', aliases=['c183', 'Devoted_Servant_4'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Devoted Servant Nana',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345145.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (500/500)', inline=False)
        embed.add_field(name='Monster Effect', value='You can Special Summon this monster from your hand if you control a "Devoted Servant" or "Mechanical Servant" monster. You can only Special Summon "Devoted Servant Nana" once per turn this way. You can shuffle 1 of your banished cards into the Deck, banish this card from the GY, and discard 1 card; Special Summon 1 "Devoted Servant" Monster from your Deck. You can only use this effect of "Devoted Servant Nana" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c183(bot))