import discord
from discord.ext import commands
from discord.utils import get

class c204(commands.Cog, name="c204"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Manoeuvre_Overwhelming_Force', aliases=['c204', 'Scorn_Operative_10'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Manoeuvre - Overwhelming Force',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348910.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='If you control a "Scorn Operative" monster that began the Duel in the Extra Deck, you can activate this card from your hand.\n● Once per your turn, when a monster effect is activated: You can Tribute 1 other "Manoeuvre -" Spell/Trap; negate that activation.\n● Once per opponent\'s turn, when a Spell/Trap Card or effect is activated: You can Tribute 1 other "Manoeuvre -" Spell/Trap; negate that activation.\nYou can only control 1 "Manoeuvre - Overwhelming Force". You can only activate 1 "Manoeuvre - Overwhelming Force" from the hand per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c204(bot))