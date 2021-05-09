import discord
from discord.ext import commands
from discord.utils import get

class c184(commands.Cog, name="c184"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Devoted_Servant\'s_Errand_Girl', aliases=['c184', 'Devoted_Servant_5'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Devoted Servant\'s Errand Girl',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345149.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Tuner/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='3 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is Normal or Special Summoned: You can add 1 "Devoted Servant" monster from your Deck to your hand. During your opponent\'s turn, if you Special Summon a monster from your hand while this card is in your Hand or GY: You can Special Summon this card, but it has its effects negated, and if you do, immediately after this effect resolves, Synchro Summon 1 Machine-Type Synchro Monster using only that monster and this card. This card is banished instead of being sent to the GY when used as a Synchro Material this way. You can only use each effect of "Devoted Servant\'s Errand Girl" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c184(bot))