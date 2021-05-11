import discord
from discord.ext import commands
from discord.utils import get

class c283(commands.Cog, name="c283"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Priestess_of_the_Seal', aliases=['c283'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Priestess of the Seal',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361026.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fairy/Union/Pendulum/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='3 (0/2000) [1/1]', inline=False)
        embed.add_field(name='Pendulum Effect', value='If your opponent controls 2 or more monsters and you control no monsters: You can Special Summon this card from your Pendulum Zone.', inline=False)
        embed.add_field(name='Monster Effect', value='Once per turn, you can either: Target 1 face-up monster on the field; equip this card to that target, OR: Unequip this card and Special Summon it in face-up Attack Position. While equipped by the effect, the equipped monster has its effects negated. but increase its DEF by 2000. If the equipped monster would be destroyed by battle or card effect, destroy this card instead.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c283(bot))