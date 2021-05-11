import discord
from discord.ext import commands
from discord.utils import get

class c257(commands.Cog, name="c257"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Yith', aliases=['c257', 'Abyssal_8'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Yith',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360319.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Insect/Flip/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='1 (0/0)', inline=False)
        embed.add_field(name='Monster Effect', value='FLIP: Draw 1 card, and if you do, reveal it, and if it is an "Abyssal" card, draw an additional card.\nYou can target 1 face-up monster you control; change it to face-down Defense Position, and if you do, Special Summon 1 "Abyssal" monster from your hand or GY, in face-up or face-down Defense Position. You can only use each effect of "Abyssal Yith" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c257(bot))