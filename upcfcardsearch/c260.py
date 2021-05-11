import discord
from discord.ext import commands
from discord.utils import get

class c260(commands.Cog, name="c260"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Yikilth_Lair_of_the_Abyssals', aliases=['c260', 'Abyssal_11'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Yikilth, Lair of the Abyssals',
                              color=0x1D9E74)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2360326.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Abyssal)', inline=True)
        embed.add_field(name='Type', value='Spell/Field', inline=False)
        embed.add_field(name='Card Effect', value='When this card is activated: Add 1 "Abyssal" monster from your Deck to your hand. Once per turn, when your opponent activates a card or effect that targets and/or would destroy a Set monster(s) you control: You can flip 1 Set monster you control into face-up Attack or Defense Position; negate the activation. You can only activate 1 "Yikilth, Lair of the Abyssals" per turn.', inline=False)
        embed.set_footer(text='Set Code: ANCF')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c260(bot))