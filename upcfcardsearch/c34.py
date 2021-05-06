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
        embed.add_field(name='Card Effect', value='When a "Hidden Treasure" monster you control would be destroyed by battle, you can discard 1 card from your hand instead. If this card is discarded: You can Special Summon 1 Rank 4 or lower Beast Xyz Monster from your GY in Defense Position, but banish it during your End Phase. You must control 2 or more Beast monsters or a "Hidden Treasure" monster to activate and resolve this effect of "Protecting the Hidden Treasure".', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c34(bot))