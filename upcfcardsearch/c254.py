import discord
from discord.ext import commands
from discord.utils import get

class c254(commands.Cog, name="c254"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Abyssal_Shoggoth', aliases=['c254', 'Abyssal_5'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Abyssal Shoggoth',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360307.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Sea Serpent/Flip/Effect (WATER)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='6 (2000/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='FLIP: You can Special Summon 1 "Abyssal Shoggoth" from your hand, Deck or GY in face-up Defense Position, and if you do, destroy 1 card on the field. You can only use this effect of "Abyssal Shoggoth" once per turn.\nOnce per turn: You can change this card to face-down Defense Position.', inline=False)
        embed.set_footer(text='Set Code: ANCF')
        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c254(bot))