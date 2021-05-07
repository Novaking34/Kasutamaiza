import discord
from discord.ext import commands
from discord.utils import get

class c194(commands.Cog, name="c194"):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
    @commands.command(name='Scorn_Operative_Eclipse', aliases=['c194', 'Scorn_Operative_1'])
    async def example_embed(self, ctx):
        embed = discord.Embed(title='Scorn Operative - Eclipse',
                              color=0xff8b53)
        embed.set_thumbnail(url='https://www.duelingbook.com/images/custom-pics/2300000/2348890.jpg')

        embed.add_field(name='Status (Archetype)', value='Casual:3/Tournament:3 (Scorn Operative)', inline=True)
        embed.add_field(name='Type (Attribute)', value='Cyberse/Effect (DARK)', inline=False)
        embed.add_field(name='Level (ATK/DEF)', value='8 (2000/2000)', inline=False)
        embed.add_field(name='Monster Effect', value='You can Special Summon this card (from your hand) by Tributing 1 "Scorn Operative" monster that began the Duel in the Extra Deck. Once while this card is face-up on the field: You can make this card lose exactly 1500 ATK. Once per turn, if this card\'s ATK on the field is reduced by a card effect: This card gains 2000 ATK, and if it does, you can return 1 "Manoeuvre -" card you control to the Deck, and if you do that, activate 1 "Manoeuvre -" Spell/Trap with a different name from your Deck. You can only Summon "Scorn Operative - Eclipse" once per turn.', inline=False)
        embed.set_footer(text='Set Code: GMMP')

        await ctx.send(embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(c194(bot))