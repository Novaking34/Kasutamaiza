import discord
from discord.ext import commands
from discord.utils import get

class c187(commands.Cog, name="c187"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Devoted_Servant\'s_Decoy_Doll', aliases=['c187', 'Devoted_Servant_9'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Devoted Servant\'s Decoy Doll',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2345154.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Devoted Servant)', inline=True)
        embed.add_field(name='Type', value='Trap/Normal', inline=False)
        embed.add_field(name='Card Effect', value='Target 1 "Devoted Servant" card in your GY and 1 card you control; return them both to the hand, then Special Summon 1 "Devoted Servant Token" (Machine/Tuner/LIGHT/Level 3/ATK 0/DEF 0) to your field in Defense Position. You can banish this card from your GY; immediately after this effect resolves, Synchro Summon 1 Machine Synchro Monster from your Extra Deck using only "Devoted Servant" monsters you control as Material. You can only use each effect of "Devoted Servant\'s Decoy Doll" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c187(bot))