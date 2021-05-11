import discord
from discord.ext import commands
from discord.utils import get

class c297(commands.Cog, name="c297"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='The_Magus_of_Explosions_Megumin', aliases=['c297'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='The Magus of Explosions Megumin',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2361144.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Effect (FIRE)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (3100/300)', inline=False)
        embed.add_field(name='Monster Effect', value='You can Special Summon this card (from your hand) by banishing 5 Spells with different names from your GY. You can only Special Summon "The Magus of Explosions Megumin" once per turn this way. If this card is Special Summoned: You can add 1 "Explosion!!!" from your Deck or GY to your hand. If this card is destroyed, you can banish this card; inflict 1000 damage to your opponent. You can only use each effect of "The Magus of Explosions Megumin" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c297(bot))