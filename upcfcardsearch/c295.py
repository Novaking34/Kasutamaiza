import discord
from discord.ext import commands
from discord.utils import get

class c295(commands.Cog, name="c295"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Blazarsaurs', aliases=['c295'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Blazarsaurs',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361138.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Dinosaur/Union/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2800/2500)', inline=False)
        embed.add_field(name='Monster Effect', value='If this card is Special Summoned: You can Special Summon 1 Dinosaur monster from your GY. You can only use this effect of "Blazarsaurs" once per turn. Once per turn, you can either: Target 1 Dinosaur monster you control; equip this card to that target, OR: Unequip this card and Special Summon it. When a card or effect is activated that targets a monster equipped with this card (Quick Effect): You can negate that effect, then send 1 card from your hand to the GY, and if you do, you can destroy 1 card on the field.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c295(bot))