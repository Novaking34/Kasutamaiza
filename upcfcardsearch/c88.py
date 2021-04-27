import discord
from discord.ext import commands
from discord.utils import get

class c88(commands.Cog, name="c88"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Unstoppable_Bond', aliases=['c88'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Unstoppable Bond',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2321529.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='Once per turn: You can Fusion Summon 1 Fusion Monster from your Extra Deck, by banishing Fusion Materials from your hand or GY, but the effects of banished cards cannot be activated this turn. If a monster Fusion Summoned by this card\'s effect would leave the field, banish it. You can banish 1 face-up Fusion Monster Summoned by this card\'s effect; if any of the Fusion Materials that were used for its Fusion Summon are banished, shuffle them into the Deck. You can only activate this effect of "Unstoppable Bond" once per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c88(bot))