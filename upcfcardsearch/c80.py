import discord
from discord.ext import commands
from discord.utils import get

class c80(commands.Cog, name="c80"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Lord_of_Parasites', aliases=['c80'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Lord of Parasites',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321510.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Equip', inline=False)
        embed.add_field(name='Card Effect', value='The equipped monster\'s effects are negated, also it gains 2000 ATK/DEF. During your Main Phase 2, if this card is in your GY and both players control the same number of monsters: You can add this card to your hand. You can only use this effect of "Lord of Parasites" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c80(bot))