import discord
from discord.ext import commands
from discord.utils import get

class c253(commands.Cog, name="c253"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Seacorpse', aliases=['c253', 'Abyssal_4'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Seacorpse',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360302.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Fish/Flip/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2000/2800)', inline=False)
        embed.add_field(name='Monster Effect', value='FLIP: You can target 1 monster on the field; destroy it, and if you do, banish it, and if you do that, inflict damage to your opponent equal to the original ATK of that monster. You can only use this effect of "Abyssal Seacorpse" once per turn.\nOnce per turn: You can change this card to face-down Defense Position.', inline=False)
        embed.set_footer(text='Set Code: ANCF')
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c253(bot))