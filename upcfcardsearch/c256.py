import discord
from discord.ext import commands
from discord.utils import get

class c256(commands.Cog, name="c256"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Wraith', aliases=['c256', 'Abyssal_7'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Wraith',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360313.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Zombie/Flip/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='7 (1500/2600)', inline=False)
        embed.add_field(name='Monster Effect', value='FLIP: You can target up to 5 cards in the GYs; banish them, then this card gains 200 ATK for each. You can only use this effect of "Abyssal Wraith" once per turn.\nOnce per turn: You can change this card to face-down Defense Position.', inline=False)
        embed.set_footer(text='Set Code: ANCF')
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c256(bot))