import discord
from discord.ext import commands
from discord.utils import get

class c166(commands.Cog, name="c166"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Spellspire_Monte', aliases=['c166', 'Spellspire_3'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Spellspire Monte',
                              color=0xFDE68A)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2344709.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Spellspire)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Spellcaster/Pendulum/Normal (LIGHT)', inline=False)
        embed.add_field(name='Level (ATK/DEF) [Pendulum Scales]', value='5 (2400/0) [6/6]', inline=False)
        embed.add_field(name='Pendulum Effect', value='You can only Pendulum Summon Spellcaster monsters. This effect cannot be negated. Each time a Spell Card is activated, place 1 Spell Counter on this card. Once per turn: You can target up to 3 cards on the field, then remove 2 Spell Counters from this card for each target; Set those cards.', inline=False)
        embed.add_field(name='Lore Text', value='Ever since he was removed from the Order of Kasutamaiza for using forbidden magic to bring him back to this world, Monte dedicated his life to become reformed. Honing all his time and energy, Monte was one of the first of the Spellspires to learn how to tame dragons. With this knowledge, the Spellspires might stand a chance against the new threats that surround them.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c166(bot))