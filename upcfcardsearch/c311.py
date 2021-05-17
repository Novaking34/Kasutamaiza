import discord
from discord.ext import commands
from discord.utils import get

class c311(commands.Cog, name="c311"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Delilah_the_Blooming_Flower', aliases=['c311'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Delilah the Blooming Flower')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361288.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Zombie/Xyz/Effect (LIGHT)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='4 (1300/2600)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Level 4 monsters\nIf this card is Xyz Summoned: You can send the top card of your Deck to the GY, then, if it was a monster, you can send 1 additional card from the top of your Deck to the GY. Once per turn (Quick Effect): You can detach 1 material from this card, then target 1 face-up card on each side of the field; destroy them, then Set the destroyed cards to the fields they were on before they were destroyed. This turn, monsters Special Summoned by this effect cannot be targeted for attacks or by card effects, also Spell/Trap Cards Set by this effect cannot be activated.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c311(bot))