import discord
from discord.ext import commands
from discord.utils import get

class c201(commands.Cog, name="c201"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Manoeuvre_Mass_Deployment', aliases=['c201', 'Scorn_Operative_8'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Manoeuvre - Mass Deployment',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348907.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='Once per turn, you can activate 1 of these effects:\n● Add 1 "Scorn Operative" card or 1 "Insurgent Resurgence" from your Deck to your hand.\n● Target 1 "Scorn Operative" monster you control; Special Summon a monster with the same original name from your Deck.\nYou can only control 1 "Manoeuvre - Mass Deployment". You can only activate 1 "Manoeuvre - Mass Deployment" from the hand per turn. You cannot activate this card the turn it was Set.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c201(bot))