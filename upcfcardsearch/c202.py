import discord
from discord.ext import commands
from discord.utils import get

class c202(commands.Cog, name="c202"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Manoeuvre_Materiel_Reclamation', aliases=['c202', 'Scorn_Operative_9'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Manoeuvre - Materiel Reclamation',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348909.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='Once per turn, you can activate 1 of these effects:\n● Target 1 "Scorn Operative" monster in your GY; Special Summon it.\n● Target 1 "Manoeuvre -" card or 1 "Insurgent Resurgence" in your GY; add it to your hand.\nYou can only control 1 "Manoeuvre - Materiel Reclamation". You can only activate 1 "Manoeuvre - Materiel Reclamation" from the hand per turn. You cannot activate this card the turn it was Set.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c202(bot))