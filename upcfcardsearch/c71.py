import discord
from discord.ext import commands
from discord.utils import get

class c71(commands.Cog, name="c71"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='An_Endless_Sparring_Match', aliases=['c71'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='An Endless Sparring Match',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321489.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: Change the battle positions of all face-up monsters to Attack Position. Once per turn, at the start of your Battle Phase: You can target 1 monster you control; this turn, that monster can attack all monsters your opponent controls once each during each Battle Phase this turn, but all battle damage taken from attacks involving that monster is halved, also other monsters you control cannot attack. Once per turn, during each Standby Phase, you must pay 700 LP while controlling 3 or more monsters, and if you cannot, destroy this card, then take 3000 damage.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c71(bot))