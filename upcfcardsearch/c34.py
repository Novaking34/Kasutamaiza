import discord
from discord.ext import commands
from discord.utils import get

class c34(commands.Cog, name="c34"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Protecting_the_Hidden_Treasure', aliases=['c34','Hidden_Treasure_10'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Protecting the Hidden Treasure',
                              color=0xBC5A84)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321347.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Hidden Treasure)', inline=True)
        embed.add_field(name='Type', value='Trap/Continuous', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: Immediately after this effect resolves, Xyz Summon 1 "Hidden Treasure" Xyz Monster, using Beast monsters from your field or GY as material (max. 2), and if you do, you cannot activate that card\'s effect this turn. Once per turn: You can target 1 Beast Xyz monster with 1 or less material; attach 1 "Hidden Treasure" monster from your hand or GY to that monster as material, but it cannot activate its effects this turn. You must control 2 or more Beast monsters or "Hidden Treasure" monsters to activate and resolve this effect of "Protecting the Hidden Treasure." You can only activate 1 "Protecting the Hidden Treasure" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c34(bot))