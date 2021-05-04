import discord
from discord.ext import commands
from discord.utils import get

class c178(commands.Cog, name="c178"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Lord_of_Phantaclysms_Diaschino', aliases=['c178', 'Phantacylsms_12'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Lord of Phantaclysms, Diaschino')
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2304691.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Phantaclysms)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Xyz/Effect (LIGHT)', inline=False)
        embed.add_field(name='Rank (ATK/DEF)', value='2 (2000/0)', inline=False)
        embed.add_field(name='Monster Effect', value='2 Level 2 "Phantaclysm" monsters\nMonsters cannot attack, except "Phantaclysm" monsters. This card can attack directly. If this card is Xyz Summoned: Return all other cards on the field to the hand. During the End Phase: You can detach 1 material from this card; both players discard cards until they have 4 in their hand. If this card is destroyed and sent to the GY: You can Special Summon 1 "Phantaclysmic" monster from your GY. You can only Summon "Lord of Phantaclysms, Diaschino" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c178(bot))