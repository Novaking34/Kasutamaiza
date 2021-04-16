import discord
from discord.ext import commands
from discord.utils import get

class c1(commands.Cog, name="c1"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Flame_Claws_Dragon', aliases=['c1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Flame-Claws Dragon',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2302879.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dragon/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='4 (1000/1500)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card attacks a Defense Position monster, inflict piercing battle damage to your opponent. If "Jaw Blades" is equipped to this card, it gains 500 ATK/DEF, but other monsters you control cannot attack. During your Main Phase: You can add 1 "Jaw Blades" from your Deck to your hand. (Quick Effect): You can target 1 card your opponent controls; destroy 1 "Jaw Blades" equipped to this card, and if you do, destroy the targeted card. You can only use each effect of "Flame-Claws Dragon" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c1(bot))