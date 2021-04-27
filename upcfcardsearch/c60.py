import discord
from discord.ext import commands
from discord.utils import get

class c60(commands.Cog, name="c60"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Machine_Lord_Servants', aliases=['c60', 'Machine_Lord_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Machine Lord Servants',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321474.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Machine Lord)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Machine/Tuner/Effect (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/800)', inline=False)
        embed.add_field(name='Monster Effect', value='(Quick Effect): Target 1 Level 6 or lower Machine monster in your GY; Special Summon it, but its effects are negated, also immediately after this effect resolves, Synchro Summon 1 Machine Synchro Monster, using this card and other monsters you control as material, but banish this card instead of sending it to the GY. You can only use the effect of "Machine Lord Servants" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c60(bot))