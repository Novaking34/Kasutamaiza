import discord
from discord.ext import commands
from discord.utils import get

class c255(commands.Cog, name="c255"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Titanice', aliases=['c255', 'Abyssal_6'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Titanice',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360311.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Rock/Flip/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (2700/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='FLIP: Destroy Spells/Traps your opponent controls, up to the number of "Abyssal" monsters you control. You can only use this effect of "Abyssal Titanice" once per turn.\nOnce per turn: You can change this card to face-down Defense Position.', inline=False)
        embed.set_footer(text='Set Code: ANCF')
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c255(bot))