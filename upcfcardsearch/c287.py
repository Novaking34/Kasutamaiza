import discord
from discord.ext import commands
from discord.utils import get

class c287(commands.Cog, name="c287"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Bringer_of_Silence', aliases=['c287'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Bringer of Silence',
                              color=0xcccccc)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361048.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Zombie/Synchro/Pendulum/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='5 (2000/0) [8/8]', inline=False)
        embed.add_field(name='Pendulum Effect', value='Your opponent cannot activate monster effects during the Battle Phase.', inline=False)
        embed.add_field(name='Monster Effect', value='1 Tuner + 1+ non-Tuner monsters\nWhen a monster on the field activates its effect, or a Spell/Trap that is already on the field activates its effect (Quick Effect): You can banish that card on the field and all cards your opponent controls in the same column as that card, then destroy this card. If this card in the Monster Zone is destroyed: You can place it in your Pendulum Zone. You can only use each effect of "Bringer of Silence", once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c287(bot))