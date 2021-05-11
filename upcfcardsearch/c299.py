import discord
from discord.ext import commands
from discord.utils import get

class c299(commands.Cog, name="c299"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Explosion!!!', aliases=['c299'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Explosion!!!',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361154.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Quick-Play', inline=False)
        embed.add_field(name='Card Effect', value='Activate only if you control a face-up Attack Position "The Magus of Explosions Megumin" (and no other monsters). Destroy all monsters OR Spell/Traps on the field, except "The Magus of Explosions Megumin", then inflict 300 damage to both players for each of their cards destroyed. You cannot conduct your Battle Phase this turn. After this card resolves, banish it face-down. You can only activate 1 "Explosion!!!" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c299(bot))