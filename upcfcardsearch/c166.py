import discord
from discord.ext import commands
from discord.utils import get

class c166(commands.Cog, name="c166"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Spellspire_Hu', aliases=['c166', 'Spellspire_2'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Spellspire Hu',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344704.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Spellspire)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Pendulum/Normal (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='3 (1550/1200) [2/2]', inline=False)
        embed.add_field(name='Pendulum Effect', value='You can only Pendulum Summon Spellcaster monsters. This effect cannot be negated. Once per turn. during your Main Phase 1: You can remove a number of Spell Counters from this card (max. 5); Special Summon 1 Spellcaster monster from your face-up Extra Deck whose Level is equal to the number of Spell Counters removed.', inline=False)
        embed.add_field(name='Lore Text', value='As one of the newer students of the Spellspire practice, Hu takes pride in his ability to conjure powerful familiars. Some say that the stars themselves even look in awe at the abilities of this young prodigy.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c166(bot))